#!/usr/bin/env python

# bt106c - main func

import re
import sys
import time
import base64
import datetime
import argparse
import multiprocessing
from types import FunctionType

#Handlers
from DbHandler import DbHandler
from CommonHandler import CommonHandler
from CheckHandler import CheckHandler


def getMethods():
    '''
    Get a dictionary of functions to loop against 'fkFunction' db field.

    :return: Return dictionary of main script functions
    :rtype: dict

    '''
    functions = {}
    for x, y in globals().items():
        if type(y) == FunctionType:
            functions[x] = y
    return functions


def listener(commonHandler, queue):
    '''
    A process with access to the log file. The listener
    gets messages from the workers and writes to the log file.
    Shutdown occurs when the 'killListener' string is put into the queue.

    :param CommonHandler commonHandler:
    :param multiprocessing.managers.AutoProxy[Queue] queue:

    '''

    streamLog = open(commonHandler.checkLogFile, 'a')

    while True:
        m = queue.get()
        msg = '%s' % (m)

        if msg == 'killListener':
            break

        if msg:
            streamLog.write(msg + '\n')

    streamLog.flush()
    streamLog.close()
    return


def variableWorker(gargoyleFunctions, isSudoWhitelistCmd, commonHandler, queue, component, checkID, checkTask, command, regex, resource, expected, checkValue, valueLogic, host, hostname, zone, zoneJson, fkFunction):
    '''
    gargoyleFunctions are used to compare to the DB fkFunction field. On
    a match the variable funcObject is executed. Log output is put into the queue for logging.

    :param dict gargoyleFunctions: Function dictionary.
    :param bool isSudoWhitelistCmd: Is the command allowed to run sudo.
    :param CommonHandler commonHandler:
    :param multiprocessing.managers.AutoProxy[Queue] queue:
    :param str component: Grouping identifier for types of checks to run.
    :param str checkID: Metadata ID.
    :param str checkTask: Metadata name.
    :param str command: Command with full path to run.
    :param str regex: Regular expression for the check.
    :param str resource: Resource to test, usually a file.
    :param str expected: Expected data to be returned. The data is cosmetic.
    :param str checkValue: Value for logical evaluation.
    :param str valueLogic: Logic to evaluate actual value, greater than or equal to 'gte', less than or equal to, 'lte', or equals 'equal'.
    :param str host: Target full FQDN.
    :param str hostname: Target hostname.
    :param str zone: Zone identifier.
    :param str fkFunction: Name of function to use
    '''

    logOutput = ''

    for funcName, funcObject in gargoyleFunctions.items():
        # if FK matches global function name
        if funcName == fkFunction:
            # Call the function string matched object
            logOutput = funcObject(commonHandler, isSudoWhitelistCmd, component, checkID, checkTask, command, regex, resource, expected, checkValue, valueLogic, host, hostname, zone, zoneJson)

    queue.put(logOutput)
    return


def setLogOutput(hostname, level, component, checkID, checkTask, cmd, resource = '', expected = '', checkValue = '', valueLogic = '', actual = '', output = '', testResult = '', bundleJson = ''):
    '''
    Format data into JSON log format

    :param str hostname: Target hostname.
    :param str level: Logging level
    :param str component: Grouping identifier for types of checks to run.
    :param str checkID: Metadata ID.
    :param str checkTask: Metadata name.
    :param str cmd: Command with full path to run.
    :param str resource: Resource to test, usually a file.
    :param str expected: Expected data to be returned. The data is cosmetic.
    :param str checkValue: Value for logical evaluation.
    :param str valueLogic: Logic to evaluate actual value, greater than or equal to 'gte', lessthan or equal to, 'lte', or equals 'equal'.
    :param str actual: Actual data returned.
    :param str output: Data.
    :param str testResult: Ideally, Pass or Fail.
    :return: Log output JSON string is returned
    :rtype: str

    '''

    # Set log time
    timeStamp = datetime.datetime.utcnow().isoformat() + 'Z'

    # data is base64 encoded to prevent syntax issues with json lua encoder
    if "'" in str(cmd) or '"' in str(cmd) or '\n' in str(cmd):
        cmd = base64.b64encode(cmd)

    if "'" in str(expected) or '"' in str(expected) or '\n' in str(expected):
        expected = base64.b64encode(expected)

    if "'" in str(checkValue) or '"' in str(checkValue) or '\n' in str(checkValue):
        checkValue = base64.b64encode(checkValue)

    if "'" in str(actual) or '"' in str(actual) or '\n' in str(actual):
        actual = base64.b64encode(actual)

    if "'" in str(output) or '"' in str(output) or '\n' in str(output):
        output = base64.b64encode(output)

    # JSON log format
    logOutput = '{"gargoyleLogType":"%s","gargoyleTimestamp":"%s","gargoyleSeverity":"%s","gargoyleHostname":"%s","gargoyleComponent":"%s","gargoyleCheckID":"%s","gargoyleTask":"%s","gargoyleCommand":"%s","gargoyleResource":"%s","gargoyleExpected":"%s","gargoyleCheckValue":"%s","gargoyleValueLogic":"%s","gargoyleActual":"%s","gargoyleOutput":"%s","gargoyleResult":"%s"}' % (
        'osgLogger',
        timeStamp,
        level,
        hostname,
        component,
        checkID,
        checkTask,
        cmd,
        resource,
        expected,
        checkValue,
        valueLogic,
        actual,
        output,
        testResult)

    return logOutput


def injectionTest(commonHandler, isSudoWhitelistCmd, component, checkID, checkTask, command, regex, resource, expected, checkValue, valueLogic, host, hostname, zone, zoneJson):
    '''
    Test command execution via bypass
    '''

    # Log file
    localLogFile = '%s/%s' % ('/var/log/gargoyle', 'injection_test.txt')
    localLogger = open(localLogFile, 'w')

    if regex:
        fullCmd = '%s \\"%s\\" %s' % (command, regex, resource)
    else:
        fullCmd = '%s %s' % (command, resource)

    sshCommand = commonHandler.getSshCommand(isSudoWhitelistCmd, fullCmd)

    # Run remote command
    lines = commonHandler.getRemoteOutput(host, sshCommand)

    if lines:
        for rawLine in lines:
            line = rawLine.encode('utf-8')
            localLogger.write(line)

    # close log file
    localLogger.close()
    return


def checkSubstrConfigParameter(commonHandler, isSudoWhitelistCmd, component, checkID, checkTask, command, regex, resource, expected, checkValue, valueLogic, host, hostname, zone, zoneJson):
    '''
    Pass if the checkValue is contained in the actual output, no split.
    Fail for all other conditions.

    The remote command is wrapped in echo quotes for piping to sudo (or not).
    Output is formatted and returned.

    :param CommonHandler commonHandler:
    :param bool isSudoWhitelistCmd: Is the command allowed to run sudo.
    :param multiprocessing.managers.AutoProxy[Queue] queue:
    :param str component: Grouping identifier for types of checks to run.
    :param str checkID: Metadata ID.
    :param str checkTask: Metadata name.
    :param str command: Command with full path to run.
    :param str regex: Regular expression for the check.
    :param str resource: Resource to test, usually a file.
    :param str expected: Expected data to be returned. The data is cosmetic.
    :param str checkValue: Value for logical evaluation.
    :param str valueLogic: Logic to evaluate actual value, greater than or equal to 'gte', lessthan or equal to, 'lte', or equals 'equal'.
    :param str host: Target full FQDN.
    :param str hostname: Target hostname.
    :param str zone: Zone identifier.
    :param str fkFunction: Name of function to use
    :return: JSON formatted string is returned.
    :rtype: str

    '''

    # set output vars
    level = ''
    actual = ''
    output = ''
    testResult = ''
    logOutput = ''

    # check if file present on remote host
    exists = commonHandler.getResourceExists(host, resource)

    # double escape regex double quote (will be inside double echo quotes)
    if regex:
        fullCmd = '%s \\"%s\\" %s' % (command, regex, resource)
    else:
        fullCmd = '%s %s' % (command, resource)


    if exists:

        sshCommand = commonHandler.getSshCommand(isSudoWhitelistCmd, fullCmd)

        lines = commonHandler.getRemoteOutput(host, sshCommand)

        out = ''

        if lines:
            if len(lines) == 1:
                out = lines[0].strip()
            else:
                out = ','.join(lines).strip()

            if out:
                actual = out.strip()
                if regex:
                    # start if regex
                    regex = '%s' % (regex)
                    checkActual = re.findall(r'' + regex + '', actual)

                    if checkActual:
                        # lower to eliminate case-mismatch FP
                        output = actual
                        out = checkActual[0].lower()
                        # check if value matches expected or expected in value, lower of no case mismatch
                        if out.lower() == checkValue.lower() or checkValue.lower() in out.lower():
                            testResult = 'Pass'
                            level = 'INFO'
                        else:
                            testResult = 'Fail'
                            level = 'CRITICAL'
                    else:
                        testResult = 'Fail'
                        level = 'CRITICAL'
                    # end if regex
                else:
                    # get cmd output
                    # lower to eliminate case-mismatch FP
                    output = actual
                    out = output.lower()
                    # check if value matches expected or expected in value, lower of no case mismatch
                    if out.lower() == checkValue.lower() or checkValue.lower() in out.lower():
                        testResult = 'Pass'
                        level = 'INFO'
                    else:
                        testResult = 'Fail'
                        level = 'CRITICAL'
            else:
                testResult = 'Fail'
                level = 'CRITICAL'
        else:
            testResult = 'Fail'
            level = 'CRITICAL'

        # format log output
        logOutput = setLogOutput(hostname, zone, zoneJson, level, component, checkID, checkTask, fullCmd, resource, expected, checkValue, valueLogic, actual, output, testResult)

    return logOutput


def checkUnsetParameter(commonHandler, isSudoWhitelistCmd, component, checkID, checkTask, command, regex, resource, expected, checkValue, valueLogic, host, hostname, zone, zoneJson):
    '''
    Pass if no data is returned or the parameter is commented out with '#'.
    Fail for all other conditions.

    The remote command is wrapped in echo quotes for piping to sudo (or not).
    Output is formatted and returned.

    :param CommonHandler commonHandler:
    :param bool isSudoWhitelistCmd: Is the command allowed to run sudo.
    :param multiprocessing.managers.AutoProxy[Queue] queue:
    :param str component: Grouping identifier for types of checks to run.
    :param str checkID: Metadata ID.
    :param str checkTask: Metadata name.
    :param str command: Command with full path to run.
    :param str regex: Regular expression for the check.
    :param str resource: Resource to test, usually a file.
    :param str expected: Expected data to be returned. The data is cosmetic.
    :param str checkValue: Value for logical evaluation.
    :param str valueLogic: Logic to evaluate actual value, greater than or equal to 'gte', lessthan or equal to, 'lte', or equals 'equal'.
    :param str host: Target full FQDN.
    :param str hostname: Target hostname.
    :param str zone: Zone identifier.
    :param str fkFunction: Name of function to use
    :return: JSON formatted string is returned.
    :rtype: str

    '''
    # set output vars
    level = ''
    actual = ''
    output = ''
    testResult = ''
    logOutput = ''

    # check if file present on remote host
    exists = commonHandler.getResourceExists(host, resource)

    # double escape regex double quote (will be inside double echo quotes)
    if regex:
        fullCmd = '%s \\"%s\\" %s' % (command, regex, resource)
    else:
        fullCmd = '%s %s' % (command, resource)

    if exists:

        sshCommand = commonHandler.getSshCommand(isSudoWhitelistCmd, fullCmd)

        lines = commonHandler.getRemoteOutput(host, sshCommand)

        out = ''

        if lines:
            if len(lines) == 1:
                out = lines[0].strip()
            else:
                out = ','.join(lines).strip()

            if out:
                actual = out.strip()

                if regex:
                    regex = '%s' % (regex)
                    checkActual = re.findall(r'' + regex + '', actual)
                else:
                    checkActual = actual

                if checkActual:

                    if regex:
                        output = checkActual[0]
                    else:
                        output = checkActual

                    if '#' in output:
                        testResult = 'Pass'
                        level = 'INFO'
                    else:
                        testResult = 'Fail'
                        level = 'CRITICAL'
                else:
                    output = 'No regex match in cmd output'
                    testResult = 'Fail'
                    level = 'CRITICAL'
            # Pass on null output
            else:
                testResult = 'Pass'
                level = 'INFO'
        # Pass on null output
        else:
            testResult = 'Pass'
            level = 'INFO'

        # format log output
        logOutput = setLogOutput(hostname, zone, zoneJson, level, component, checkID, checkTask, fullCmd, resource, expected, checkValue, valueLogic, actual, output, testResult)

    return logOutput


def checkValueConfigParameter(commonHandler, isSudoWhitelistCmd, component, checkID, checkTask, command, regex, resource, expected, checkValue, valueLogic, host, hostname, zone, zoneJson):
    '''
    Pass if the checkValue is identical or contained in the actual value, split on the '='.
    Fail for all other conditions.

    The remote command is wrapped in echo quotes for piping to sudo (or not).
    Output is formatted and returned.

    :param CommonHandler commonHandler:
    :param bool isSudoWhitelistCmd: Is the command allowed to run sudo.
    :param multiprocessing.managers.AutoProxy[Queue] queue:
    :param str component: Grouping identifier for types of checks to run.
    :param str checkID: Metadata ID.
    :param str checkTask: Metadata name.
    :param str command: Command with full path to run.
    :param str regex: Regular expression for the check.
    :param str resource: Resource to test, usually a file.
    :param str expected: Expected data to be returned. The data is cosmetic.
    :param str checkValue: Value for logical evaluation.
    :param str valueLogic: Logic to evaluate actual value, greater than or equal to 'gte', lessthan or equal to, 'lte', or equals 'equal'.
    :param str host: Target full FQDN.
    :param str hostname: Target hostname.
    :param str zone: Zone identifier.
    :param str fkFunction: Name of function to use
    :return: JSON formatted string is returned.
    :rtype: str

    '''
    # set output vars
    level = ''
    actual = ''
    output = ''
    testResult = ''
    logOutput = ''

    # check if file present on remote host
    exists = commonHandler.getResourceExists(host, resource)

    # double escape regex double quote (will be inside double echo quotes)
    fullCmd = '%s \\"%s\\" %s' % (command, regex, resource)

    if exists:

        sshCommand = commonHandler.getSshCommand(isSudoWhitelistCmd, fullCmd)

        lines = commonHandler.getRemoteOutput(host, sshCommand)

        out = ''

        if lines:
            if len(lines) == 1:
                out = lines[0].strip()
            else:
                out = ','.join(lines).strip()

            if out:
                actual = out.strip()
                regex = '%s' % (regex)
                checkActual = re.findall(r'' + regex + '', actual)

                if checkActual:

                    # split output on the = to check value
                    p = checkActual[0].split('=')

                    # log metadata
                    output = p[1].strip()

                    # check if value matches expected or expected in value, lower of no case mismatch
                    out = p[1].strip().lower()
                    if out.lower() == checkValue.lower() or checkValue.lower() in out.lower():
                        testResult = 'Pass'
                        level = 'INFO'
                    else:
                        testResult = 'Fail'
                        level = 'CRITICAL'
                else:
                    testResult = 'Fail'
                    level = 'CRITICAL'
            else:
                testResult = 'Fail'
                level = 'CRITICAL'
        else:
            testResult = 'Fail'
            level = 'CRITICAL'

        # format log output
        logOutput = setLogOutput(hostname, zone, zoneJson, level, component, checkID, checkTask, fullCmd, resource, expected, checkValue, valueLogic, actual, output, testResult)

    return logOutput


def checkFileSystemSecurity(commonHandler, isSudoWhitelistCmd, component, checkID, checkTask, command, regex, resource, expected, checkValue, valueLogic, host, hostname, zone, zoneJson):
    '''
    Check file permissions and/or user,group ownership.

    Pass if the expected value is identical to actual value.
    Fail for all other conditions.

    The remote command is wrapped in echo quotes for piping to sudo (or not).
    Output is formatted and returned.

    :param CommonHandler commonHandler:
    :param bool isSudoWhitelistCmd: Is the command allowed to run sudo.
    :param multiprocessing.managers.AutoProxy[Queue] queue:
    :param str component: Grouping identifier for types of checks to run.
    :param str checkID: Metadata ID.
    :param str checkTask: Metadata name.
    :param str command: Command with full path to run.
    :param str regex: Regular expression for the check.
    :param str resource: Resource to test, usually a file.
    :param str expected: Expected data to be returned. The data is cosmetic.
    :param str checkValue: Value for logical evaluation.
    :param str valueLogic: Logic to evaluate actual value, greater than or equal to 'gte', lessthan or equal to, 'lte', or equals 'equal'.
    :param str host: Target full FQDN.
    :param str hostname: Target hostname.
    :param str zone: Zone identifier.
    :param str fkFunction: Name of function to use
    :return: JSON formatted string is returned.
    :rtype: str

    '''
    actual = ''
    output = ''
    testResult = ''
    logOutput = ''

    # check if file present on remote host
    exists = commonHandler.getResourceExists(host, resource)

    if exists:
        fullCmd = '%s %s' % (command, resource)

        sshCommand = commonHandler.getSshCommand(isSudoWhitelistCmd, fullCmd)

        lines = commonHandler.getRemoteOutput(host, sshCommand)

        if lines:
            if len(lines) == 1:
                out = lines[0].strip()
            else:
                out = ','.join(lines).strip()

            # Validate command output
            if out:
                actual = out.strip()
                checkActual = re.findall(r'' + regex + '', actual)

                # If output
                if checkActual:
                    # If expected permissions in findall
                    testResult = 'Pass'
                    level = 'INFO'

                # If no match of output
                else:
                    testResult = 'Fail'
                    level = 'CRITICAL'

            # If no cmd output from grep
            else:
                testResult = 'Fail'
                level = 'CRITICAL'

            logOutput = setLogOutput(hostname, zone, zoneJson, level, component, checkID, checkTask, fullCmd, resource, expected, checkValue, valueLogic, actual, output, testResult)

    return logOutput


def failIfAllListInLine(commonHandler, isSudoWhitelistCmd, component, checkID, checkTask, command, regex, resource, expected, checkValue, valueLogic, host, hostname, zone, zoneJson):
    '''
    Check resource for application GUI.

    Pass if no output.
    Fail if string found.

    The remote command is wrapped in echo quotes for piping to sudo (or not).
    Output is formatted and returned.

    :param CommonHandler commonHandler:
    :param bool isSudoWhitelistCmd: Is the command allowed to run sudo.
    :param multiprocessing.managers.AutoProxy[Queue] queue:
    :param str component: Grouping identifier for types of checks to run.
    :param str checkID: Metadata ID.
    :param str checkTask: Metadata name.
    :param str command: Command with full path to run.
    :param str regex: Regular expression for the check.
    :param str resource: Resource to test, usually a file.
    :param str expected: Expected data to be returned. The data is cosmetic.
    :param str checkValue: Value for logical evaluation.
    :param str valueLogic: Logic to evaluate actual value, greater than or equal to 'gte', lessthan or equal to, 'lte', or equals 'equal'.
    :param str host: Target full FQDN.
    :param str hostname: Target hostname.
    :param str zone: Zone identifier.
    :param str fkFunction: Name of function to use
    :return: JSON formatted string is returned.
    :rtype: str

    '''

    actual = ''
    testResult = ''
    output = ''
    logOutput = ''
    level = 'INFO'
    testResult = 'Pass'

    searchValues = checkValue.split(',')

    if regex:
        fullCmd = '%s \\"%s\\" %s' % (command, regex, resource)
    else:
        fullCmd = '%s %s' % (command, resource)

    sshCommand = commonHandler.getSshCommand(isSudoWhitelistCmd, fullCmd)

    lines = commonHandler.getRemoteOutput(host, sshCommand)

    if lines:
        for line in lines:
            if all(values.lower() in line.lower() for values in searchValues):
                actual = line.strip()
                level = 'CRITICAL'
                testResult = 'Fail'

    # Set to JSON format for Heka ES
    logOutput = setLogOutput(hostname, zone, zoneJson, level, component, checkID, checkTask, fullCmd, resource, expected, checkValue, valueLogic, actual, output, testResult)

    return logOutput


def passIfAllListInLine(commonHandler, isSudoWhitelistCmd, component, checkID, checkTask, command, regex, resource, expected, checkValue, valueLogic, host, hostname, zone, zoneJson):
    '''
    Check resource for application GUI.

    Pass if no output.
    Fail if string found.

    The remote command is wrapped in echo quotes for piping to sudo (or not).
    Output is formatted and returned.

    :param CommonHandler commonHandler:
    :param bool isSudoWhitelistCmd: Is the command allowed to run sudo.
    :param multiprocessing.managers.AutoProxy[Queue] queue:
    :param str component: Grouping identifier for types of checks to run.
    :param str checkID: Metadata ID.
    :param str checkTask: Metadata name.
    :param str command: Command with full path to run.
    :param str regex: Regular expression for the check.
    :param str resource: Resource to test, usually a file.
    :param str expected: Expected data to be returned. The data is cosmetic.
    :param str checkValue: Value for logical evaluation.
    :param str valueLogic: Logic to evaluate actual value, greater than or equal to 'gte', lessthan or equal to, 'lte', or equals 'equal'.
    :param str host: Target full FQDN.
    :param str hostname: Target hostname.
    :param str zone: Zone identifier.
    :param str fkFunction: Name of function to use
    :return: JSON formatted string is returned.
    :rtype: str

    '''

    actual = ''
    testResult = ''
    output = ''
    logOutput = ''
    level = 'CRITICAL'
    testResult = 'Fail'

    searchValues = checkValue.split(',')

    if regex:
        fullCmd = '%s \\"%s\\" %s' % (command, regex, resource)
    else:
        fullCmd = '%s %s' % (command, resource)

    sshCommand = commonHandler.getSshCommand(isSudoWhitelistCmd, fullCmd)

    lines = commonHandler.getRemoteOutput(host, sshCommand)

    if lines:
        for line in lines:
            if all(values.lower() in line.lower() for values in searchValues):
                actual = line.strip()
                level = 'INFO'
                testResult = 'Pass'

    # Set to JSON format for Heka ES
    logOutput = setLogOutput(hostname, zone, zoneJson, level, component, checkID, checkTask, fullCmd, resource, expected, checkValue, valueLogic, actual, output, testResult)

    return logOutput


def main(gargoyleFunctions):
    '''
    The main function.

    The db is opened.
    The multiprocessing pool is created.
    A list of hosts is passed to the script.
    The hostname is determined from the FQDN.
    The list of checks is returned from the DB based on the role type in the hostname.
    Command string fields are examined for injection characters and terms.
    The command is evaluated for sudo priv escalation.
    The workers are added to the multiprocessing pool.
    When the workers are done, the listener is closed.
    The pool is closed.
    The db connection is closed.

    :param dict gargoyleFunctions: Dictionary of function names and objects
    '''

    # help
    parser = argparse.ArgumentParser(description='Run SVT checks against host list')
    parser.add_argument('-p', metavar='component', nargs='?', required=False, const='opssimple', help='Print component checklist. Default: opssimple',)
    parser.add_argument('-c', metavar='component', nargs='?', required=False, const='opssimple', help='Test by component. Default: opssimple; If the flag is not set, run all checks based on the hostname role regex.',)
    parser.add_argument('-u', '--user_name', required=True, help='SSH Username',)
    parser.add_argument('-n', '--node_list', required=True, help='Path to node list',)
    args = parser.parse_args()

    hostFile = ''

    # Assign cli args
    if args.p is not None:
        printHosts = args.p
        db = DbHandler()
        chk = CheckHandler(db.cursor)
        chk.printChecks(printHosts,cloud)
        db.conn.close()
        sys.exit()

    if args.user_name is None:
        print 'Username required'
        sys.exit()
    else:
        userName = args.user_name

    if args.c is not None:
        singleTest = args.i
    else:
        singleTest = False

    if args.node_list is not None:
        hostFile = args.node_list

    # common handler
    commonHandler = CommonHandler(userName)

    # Get dbHandler handler
    dbHandler = DbHandler()

    # Set mp vars
    cpuCount = multiprocessing.cpu_count()
    if cpuCount == 1:
        print 'ERROR: You need at least 2 processors to run this script.'
        sys.exit()

    pool = multiprocessing.Pool(processes=cpuCount)

    # Initiate hosts
    hosts = []

    if not hostFile:
        hosts = commonHandler.getHosts('all')

    if hostFile:
        with open(hostFile, 'r') as f:
            hosts = f.readlines()

    # for list of workers
    securityWorkers = []

    # for host checks
    securityChecks = {}

    # Setup wp queue listener
    manager = multiprocessing.Manager()
    queue = manager.Queue()
    watcher = pool.apply_async(listener, args=(commonHandler, queue,))

    # security check handler
    checkHandler = CheckHandler(dbHandler.cursor)

    # Set all hostname checks in securityChecks
    for host in hosts:
        host = host.strip()
        hostname = commonHandler.getHostname(host)

        # Set hostname for check selection
        securityChecks[host] = []

        # Fill up host dictionary with checks
        if singleTest:
            securityChecks[host].append(list(checkHandler.getChecks(singleTest)))
        else:
            securityChecks[host].append(list(checkHandler.getChecks('identity')))
            securityChecks[host].append(list(checkHandler.getChecks('dashboard')))
            securityChecks[host].append(list(checkHandler.getChecks('compute')))
            securityChecks[host].append(list(checkHandler.getChecks('blockStorage')))
            securityChecks[host].append(list(checkHandler.getChecks('objectStorage')))
            securityChecks[host].append(list(checkHandler.getChecks('networking')))
            securityChecks[host].append(list(checkHandler.getChecks('imageStorage')))

    # Loop through accumulated checks for injection
    for host, checkList in securityChecks.iteritems():
        host = host.strip()
        hostname = commonHandler.getHostname(host)

        for dbHandlerRow in checkList:

            for row in dbHandlerRow:

                blacklistSafe = commonHandler.areFieldsBlacklistSafe([row[4], row[5], row[6]])

                if blacklistSafe:

                    component = row[1]
                    checkID = row[2]
                    checkTask = row[3]
                    command = row[4]
                    regex = row[5]
                    resource = row[6]
                    expected = row[7]
                    checkValue = row[8]
                    valueLogic = row[9]
                    fkFunction = row[10]

                    isAllowed = commonHandler.isAllowed(command)

                    if isAllowed:
                        isSudoWhitelistCmd = commonHandler.isSudoWhitelist(command)

                        securityWorker = pool.apply_async(variableWorker, args=(gargoyleFunctions, isSudoWhitelistCmd, commonHandler, queue, component, checkID, checkTask, command, regex, resource, expected, checkValue, valueLogic, host, hostname, zone, zoneJson, fkFunction))
                        securityWorkers.append(securityWorker)

                    else:
                        queue.put('killListener')
                        # Close pool, return
                        pool.close()
                        pool.join()
                        # Bail out
                        sys.exit()
                else:
                    queue.put('killListener')
                    # Close pool, return
                    pool.close()
                    pool.join()
                    # Bail out
                    sys.exit()

    for work in securityWorkers:
        work.get()

    # wrap it up
    queue.put('killListener')

    # Close and return procs
    pool.close()
    pool.join()

    # close dbHandler connection
    dbHandler.conn.close()
    return


if __name__ == '__main__':
    gargoyleFunctions = getMethods()
    main(gargoyleFunctions)
