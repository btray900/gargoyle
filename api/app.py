from flask import Flask
import pymysql
import os
import ssl
from flask import jsonify
from flask import flash, request
from flask_basicauth import BasicAuth
import sys

app = Flask(__name__)

dbHost = 'g-db'
uid = os.environ['DB_USER']
pw = os.environ['DB_PW']
database = 'osg'

dbInfo = {
    'checks': {
        'tableName': 'securityChecks',
        'fields': [
            'checkID',
            'checkTask',
            'checkValue',
            'command',
            'component',
            'enabled',
            'expected',
            'fkFunction',
            'info',
            'regex',
            'resource',
            'checkValue',
            'valueLogic',
        ],
        'dupeChkFields': [
            'component',
            'checkTask',
            'checkID',
            'command',
            'regex',
            'resource',
            'expected'
        ]
    },
    'patterns': {
        'tableName': 'checkPatterns',
        'fields': [
            'type',
            'pattern',
            'components'
            ],
        'dupeChkFields': [
            'type',
            'pattern',
            'components'
        ]
    }
}

app.config['BASIC_AUTH_USERNAME'] = os.environ['API_USER']
app.config['BASIC_AUTH_PASSWORD'] = os.environ['API_PW']

basic_auth = BasicAuth(app)

##########################################################
###                       V2                           ###
##########################################################

# create row
@app.route('/v2/<string:dbtable>', methods=['POST'])
@basic_auth.required
def createRow(dbtable):
    table = dbInfo[dbtable]['tableName']
    try:
        _json = request.json

        # to insert
        sql = 'INSERT INTO %s SET ' % table

        # duplicate check
        countSql = "SELECT id FROM %s WHERE " % table

        for field in dbInfo[dbtable]['fields']:
            for key in _json:
                if key == field:
                    # build insert query
                    str = "%s = '%s'," % (field, _json[key])
                    sql = sql + str
                    # build discreet check for duplicate entry
                    for checkColumn in dbInfo[dbtable]['dupeChkFields']:
                        if key == checkColumn:
                            dstr = "%s = '%s' AND " % (checkColumn, _json[key])
                            countSql = countSql + dstr

        # clean statement
        sql = sql.strip(',')
        countSql = countSql.strip(' AND ')

        if request.method == 'POST':
            db = pymysql.connect(dbHost,
                                 uid,
                                 pw,
                                 database,
                                 ssl={'key': '/app/gargoyleClientDb.key.pem',
                                      'cert': '/app/gargoyleClientDb.crt.pem',
                                       'ca': '/app/gargoyleRootCA.crt.pem'})

            # replace python/requests/json unescaping of required sql escapes
            if dbtable == 'checks':
                escapedCountSql = countSql.replace('\s', '\\\s').replace('\"', '\\\\"')
            elif dbtable == 'patterns':
                escapedCountSql = countSql.replace('\d', '\\\d')
            else:
                escapedCountSql = countSql

            countCursor = db.cursor(pymysql.cursors.DictCursor)
            countCursor.execute(escapedCountSql)
            count = countCursor.fetchall()
            countCursor.close()

            if len(count) == 0:
                # replace python/requests/json unescaping of required sql escapes
                if dbtable == 'checks':
                    escapedSql = sql.replace('\s', '\\\s').replace('\"', '\\\\"')
                elif dbtable == 'patterns':
                    escapedSql = sql.replace('\d', '\\\d')
                else:
                    escapedSql = sql
                print(escapedSql, flush=True)
                try:
                    cursor = db.cursor()
                    cursor.execute(escapedSql)
                    db.commit()
                    cursor.close()
                    db.close()
                    message = {'status': 'OK', 'message': '%s created successfully.' % dbtable.capitalize().strip('s')}
                except pymysql.Error as e:
                    print(e, flush=True)
                    message = {'status': 'ERROR', 'message': 'Run: docker logs cloudcom-api'}
            else:
                message = {'status': 'OK', 'message': '%s already exists in database, skipping...' % dbtable.capitalize().strip('s')}

            resp = jsonify(message)
            resp.headers['Content-Security-Policy'] = "default-src 'self';"
            resp.headers['X-XSS-Protection'] = "1; mode=block"
            resp.headers['Strict-Transport-Security'] = "max-age=3156000; includeSubDomains"
            resp.headers['X-Frame-Options'] = "SAMEORIGIN"
            resp.headers['X-Content-Type'] = "nosniff"
            resp.headers['Server'] = "unknown"
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e, flush=True)


# read/update one row by id
@app.route('/v2/<string:dbtable>/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@basic_auth.required
def doOneRowById(dbtable, id):
    table = dbInfo[dbtable]['tableName']

    if request.method == 'PUT':    # UPDATE BY ID
        try:
            _json = request.json

            sql = 'UPDATE %s SET ' % table
            for field in dbInfo[dbtable]['fields']:
                for key in _json:
                    if key in field:
                        str = "%s = '%s'," % (field, _json[key])
                        sql = sql + str
            sql = sql.strip(',')
            sql = '%s WHERE id = %s' % (sql, id)

            # replace python/requests/json unescaping of required sql escapes
            if dbtable == 'checks':
                escapedSql = sql.replace('\s', '\\\s').replace('\"', '\\\\"')
            elif dbtable == 'patterns':
                escapedSql = sql.replace('\d', '\\\d')
            else:
                escapedSql = sql

            try:
                db = pymysql.connect(dbHost,
                                     uid,
                                     pw,
                                     database,
                                     ssl={'key': '/app/gargoyleClientDb.key.pem',
                                          'cert': '/app/gargoyleClientDb.crt.pem',
                                          'ca': '/app/gargoyleRootCA.crt.pem'})

                cursor = db.cursor()
                cursor.execute(escapedSql)
                db.commit()
                cursor.close()
                db.close()
                message = {'status': 'OK', 'message': 'Check %s updated successfully.' % id}
            except pymysql.Error as e:
                print(e, flush=True)
                message = {'status': 'ERROR', 'message': 'Run: docker logs cloudcom-api'}

            resp = jsonify(message)
            resp.headers['Content-Security-Policy'] = "default-src 'self';"
            resp.headers['X-XSS-Protection'] = "1; mode=block"
            resp.headers['Strict-Transport-Security'] = "max-age=3156000; includeSubDomains"
            resp.headers['X-Frame-Options'] = "SAMEORIGIN"
            resp.headers['X-Content-Type'] = "nosniff"
            resp.headers['Server'] = "unknown"
            resp.status_code = 200
            return resp
        except Exception as e:
            print(e, flush=True)
    elif request.method == 'GET':    # READ BY ID
        try:
            try:
                db = pymysql.connect(dbHost,
                                     uid,
                                     pw,
                                     database,
                                     ssl={'key': '/app/gargoyleClientDb.key.pem',
                                          'cert': '/app/gargoyleClientDb.crt.pem',
                                          'ca': '/app/gargoyleRootCA.crt.pem'})

                cursor = db.cursor(pymysql.cursors.DictCursor)
                cursor.execute('SELECT * FROM %s WHERE id = %s' % (table, id))
                row = cursor.fetchone()
                message = {'status': 'OK', 'payload': row}
            except pymysql.Error as e:
                print(e, flush=True)
                message = {'status': 'ERROR', 'payload': 'Run: docker logs cloudcom-api'}

            resp = jsonify(message)
            resp.headers['Content-Security-Policy'] = "default-src 'self'"
            resp.headers['X-XSS-Protection'] = "1; mode=block"
            resp.headers['Strict-Transport-Security'] = "max-age=3156000; includeSubDomains"
            resp.headers['X-Frame-Options'] = "SAMEORIGIN"
            resp.headers['X-Content-Type'] = "nosniff"
            resp.headers['Server'] = "unknown"
            resp.status_code = 200
            return resp
        except Exception as e:
            print(e, flush=True)
        finally:
            cursor.close()
            db.close()
    elif request.method == 'DELETE':    # DELETE BY ID
        try:
            try:
                db = pymysql.connect(dbHost,
                                     uid,
                                     pw,
                                     database,
                                     ssl={'key': '/app/gargoyleClientDb.key.pem',
                                          'cert': '/app/gargoyleClientDb.crt.pem',
                                          'ca': '/app/gargoyleRootCA.crt.pem'})

                cursor = db.cursor()
                cursor.execute('DELETE FROM %s WHERE id = %s' % (table, id))
                db.commit()
                cursor.close()
                db.close()
                message = {'status': 'OK', 'message': '%s %s deleted successfully.' % (dbtable.capitalize().strip('s'), id)}
            except pymysql.Error as e:
                print(e, flush=True)
                message = {'status': 'ERROR', 'message': 'Run: docker logs cloudcom-api'}

            resp = jsonify(message)
            resp.headers['Content-Security-Policy'] = "default-src 'self';"
            resp.headers['X-XSS-Protection'] = "1; mode=block"
            resp.headers['Strict-Transport-Security'] = "max-age=3156000; includeSubDomains"
            resp.headers['X-Frame-Options'] = "SAMEORIGIN"
            resp.headers['X-Content-Type'] = "nosniff"
            resp.headers['Server'] = "unknown"
            resp.status_code = 200
            return resp
        except Exception as e:
            print(e, flush=True)
    else:
        return not_found()


# read all rows
@app.route('/v2/<string:dbtable>', methods=['GET'])
@basic_auth.required
def getAllRows(dbtable):
    table = dbInfo[dbtable]['tableName']
    try:
        try:
            db = pymysql.connect(dbHost,
                                 uid,
                                 pw,
                                 database,
                                 ssl={'key': '/app/gargoyleClientDb.key.pem',
                                      'cert': '/app/gargoyleClientDb.crt.pem',
                                      'ca': '/app/gargoyleRootCA.crt.pem'})

            cursor = db.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM %s ORDER BY id ASC" % (table))
            rows = cursor.fetchall()
            count = len(rows)
            message = {'status': 'OK', 'payload': rows, 'count': count}
        except pymysql.Error as e:
            print(e, flush=True)
            message = {'status': 'ERROR', 'payload': 'Run: docker logs cloudcom-api'}

        resp = jsonify(message)
        resp.headers['Content-Security-Policy'] = "default-src 'self';"
        resp.headers['X-XSS-Protection'] = "1; mode=block"
        resp.headers['Strict-Transport-Security'] = "max-age=3156000; includeSubDomains"
        resp.headers['X-Frame-Options'] = "SAMEORIGIN"
        resp.headers['X-Content-Type'] = "nosniff"
        resp.headers['Server'] = "unknown"
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e, flush=True)
    finally:
        cursor.close()
        db.close()



#################
#      404      #
#################
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.headers['Content-Security-Policy'] = "default-src 'self';"
    resp.headers['X-XSS-Protection'] = "1; mode=block"
    resp.headers['Strict-Transport-Security'] = "max-age=3156000; includeSubDomains"
    resp.headers['X-Frame-Options'] = "SAMEORIGIN"
    resp.headers['X-Content-Type'] = "nosniff"
    resp.headers['Server'] = "unknown"
    resp.status_code = 404
    return resp


#################
#      500      #
#################
@app.errorhandler(500)
def not_good(error=None):
    message = {
        'status': 500,
        'message': 'Not good: ' + request.url,
    }
    resp = jsonify(message)
    resp.headers['Content-Security-Policy'] = "default-src 'self';"
    resp.headers['X-XSS-Protection'] = "1; mode=block"
    resp.headers['Strict-Transport-Security'] = "max-age=3156000; includeSubDomains"
    resp.headers['X-Frame-Options'] = "SAMEORIGIN"
    resp.headers['X-Content-Type'] = "nosniff"
    resp.headers['Server'] = "unknown"
    resp.status_code = 500
    return resp


if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('gargoyleServer.crt.pem', 'gargoyleServer.key.pem')
    app.run(host='0.0.0.0', port='5000', ssl_context=(context))
