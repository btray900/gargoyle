#!/usr/bin/env python

# bt106c - CheckHandler class
# Handler for gargoyle


class CheckHandler:

    def __init__(self, cursor):
        self.cursor = cursor
        return

    # Get applicable checks
    def getChecks(self, component, cloud):
        select = "SELECT * FROM securityChecks WHERE component = '%s' AND cloud = '%s' AND enabled = 1" % (component, cloud)  # nosec
        self.cursor.execute(select)  # nosec
        checks = self.cursor.fetchall()
        return checks

    def getReports(self, cloud):
        select = "SELECT checkTask, component FROM securityChecks WHERE cloud = '%s'" % (cloud)  # nosec
        self.cursor.execute(select)  # nosec
        reports = self.cursor.fetchall()
        return reports
