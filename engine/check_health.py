#!/usr/bin/env python3

import os
import time
import json
import shlex
import requests
import subprocess


kibana_host = os.environ['KIBANA_HOST']
kibana_backport = os.environ['KIBANA_BACKPORT']
kibana_user = os.environ['ELASTIC_USER']
kibana_pw = os.environ['ELASTIC_PW']
kibana_url = f'https://{kibana_host}:{kibana_backport}'

status_url = f'{kibana_url}/api/status'

status = 'red'

while 'green' not in status:
    print('status is %s' % status)
    print('waiting 15 seconds for kibana to be green...')
    time.sleep(90)
    try:
        r = requests.get(f'{status_url}/api/status', auth=(kibana_user, kibana_pw), verify='/etc/ssl/certs/')
        data = json.loads(r.content)
        status = data['status']['overall']['state']
        print('KIBANA STATUS: %s' % status)
    except(Exception) as e:
        print(e)
        time.sleep(15)
        status = 'red'

try:
    print('Continue to setup dashboard')
    subprocess.check_output(shlex.split('/usr/local/bin/python3 /tmp/setup_dashboard.py'), shell=False)
except(Exception) as e:
    print(e)
