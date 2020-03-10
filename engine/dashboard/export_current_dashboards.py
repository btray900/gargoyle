#!/usr/bin/env python3

import os
import json
import subprocess
import shlex

kibana_user = os.environ['KIBANA_USER']
kibana_pw = os.environ['KIBANA_PW']
kibana_host = os.environ['KIBANA_HOST']
kibana_backport = os.environ['KIBANA_BACKPORT']
kibana_url = f'https://{kibana_host}:{kibana_backport}'


cmd = f'curl -s -XGET -u {kibana_user}:{kibana_pw} {kibana_url}/api/saved_objects/_find?type=dashboard'

o = subprocess.check_output(shlex.split(cmd), shell=False)

data = json.loads(o)

export_url = f'{kibana_url}/api/kibana/dashboards/export'

for i in data['saved_objects']:

    title = i['attributes']['title']

    title = title.replace(' ','-')

    file = f'dashboard_{title}.json'

    id = i['id']

    cmd1 = f'cp ./{file} ./old.{file}'

    subprocess.call(shlex.split(cmd1), shell=False)

    cmd2 = f'curl -s -XGET -u {kibana_user}:{kibana_pw} {export_url}?dashboard={id} -o ./{file}'

    subprocess.check_output(shlex.split(cmd2), shell=False)

    print(f'Export done for {id}:{file}')
