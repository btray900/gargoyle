#!/usr/bin/env python3
# create the dashboard

import os
import glob
import time
import json
import requests

def main():

    kibana_host = os.environ['KIBANA_HOST']
    kibana_backport = os.environ['KIBANA_BACKPORT']
    kibana_user = os.environ['ELASTIC_USER']
    kibana_pw = os.environ['ELASTIC_PW']
    kibana_url = f'https://{kibana_host}:{kibana_backport}'

    headers = {'kbn-xsrf':'true', 'Content-Type':'application/json'}

    # import dashboards
    os.chdir("/tmp")

    print('SETTING UP DASHBOARD')

    for file in glob.glob("dashboard_*.json"):

        with open(file, 'r') as f:
            dashboard = f.read()

        import_url = f'{kibana_url}/api/kibana/dashboards/import'

        r = requests.post(import_url,
                          auth=(kibana_user, kibana_pw),
                          headers=headers,
                          data=dashboard,
                          verify='/etc/ssl/certs')

        print(r.content)

        print(f'{file} created')

        time.sleep(2)

    with open('default.json' ,'r') as d:
        default_index = d.read()

    default_index_url = f'{kibana_url}/api/kibana/settings/defaultIndex'

    r = requests.post(default_index_url,
                      auth=(kibana_user, kibana_pw),
                      headers=headers,
                      data=default_index,
                      verify='/etc/ssl/certs')

    print(r.content)
    print(' ... default Index set.')

if __name__ == '__main__':
    main()
