from flask import Flask
import pymysql
from flask import jsonify
from flask import flash, request

app = Flask(__name__)

dbHost = 'db'
uid = 'root'
pw = 'xxxxFAKEPASSWDxxxx'
database = 'osg'

checkTable = 'securityChecks'

columns = [
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
]

# GET components for argparse

@app.route('/api/v1/components', methods=['GET'])
def all_components():
    try:
        db = pymysql.connect(dbHost, uid, pw, database)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT DISTINCT component FROM %s' % checkTable)
        rows = cursor.fetchall()
        components = ''
        for row in rows:
            components += '%s,' % row['component']
        message = {'status': 'OK', 'payload': components.strip(',')}
        resp = jsonify(message)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


# READ checks
@app.route('/api/v1/checks', methods=['GET'])
def all_checks():
    try:
        db = pymysql.connect(dbHost, uid, pw, database)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM %s' % checkTable)
        rows = cursor.fetchall()
        message = {'status': 'OK', 'payload': rows}
        resp = jsonify(message)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


# READ checks by component
@app.route('/api/v1/checks/<component>', methods=['GET'])
def checks(component):
    try:
        db = pymysql.connect(dbHost, uid, pw, database)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM %s WHERE component = '%s'" % (checkTable, component))
        rows = cursor.fetchall()
        message = {'status': 'OK', 'payload': rows}
        resp = jsonify(message)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


# CREATE check
@app.route('/api/v1/check', methods=['POST'])
def add_check():
    try:
        _json = request.json

        sql = 'INSERT INTO %s SET ' % checkTable
        for column in columns:
            for x in _json:
                if x in column:
                    str = "%s = '%s'," % (column, _json[x])
                    sql = sql + str
        sql = sql.strip(',')

        if request.method == 'POST':
            db = pymysql.connect(dbHost, uid, pw, database)
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            message = {'status': 'OK', 'message': 'Check added successfully.'}
            resp = jsonify(message)
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


# READ check
@app.route('/api/v1/check/<int:id>', methods=['GET'])
def check(id):
    try:
        db = pymysql.connect(dbHost, uid, pw, database)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM %s WHERE id = %s' % (checkTable, id))
        row = cursor.fetchone()
        message = {'status': 'OK', 'payload': row}
        resp = jsonify(message)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


# UPDATE check
@app.route('/api/v1/check/<int:id>', methods=['POST'])
def update_check(id):
    try:
        _json = request.json

        sql = 'UPDATE %s SET ' % checkTable
        for column in columns:
            for x in _json:
                if x in column:
                    str = "%s = '%s'," % (column, _json[x])
                    sql = sql + str
        sql = sql.strip(',')
        sql = '%s WHERE id = %s' % (sql, id)

        if request.method == 'POST':
            db = pymysql.connect(dbHost, uid, pw, database)
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            message = {'status': 'OK', 'message': 'Check updated successfully.'}
            resp = jsonify(message)
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


# DELETE check
@app.route('/api/v1/check/<int:id>', methods=['DELETE'])
def delete_check(id):
    try:
        db = pymysql.connect(dbHost, uid, pw, database)
        cursor = db.cursor()
        cursor.execute('DELETE FROM %s WHERE id = %s' % (checkTable, id))
        db.commit()
        message = {'status': 'OK', 'message': 'Check deleted successfully.'}
        resp = jsonify(message)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

