#!/usr/bin/env python

# bt106c - DbHandler class

import MySQLdb

class DbHandler:

    def __init__(self):

        self.DB_CONFIG = {
            'name': 'osg',
            'host': 'db',
            'user': 'osg',
            'pass': 'xxxFAKEPASSWDxxx'
            }

        self.conn = self.getConn()
        self.cursor = self.conn.cursor()
        return


    def getConn(self):
        conn = MySQLdb.connect(
            host = self.DB_CONFIG['host'],
            port = 3306,
            user = self.DB_CONFIG['user'],
            passwd = self.DB_CONFIG['pass'],
            db = self.DB_CONFIG['name'],
            charset='utf8',
            use_unicode=True,
        )
        return conn
