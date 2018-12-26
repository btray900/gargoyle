#!/usr/bin/env python
# create the dashboard
# bt106c

import subprocess
import glob
import time
import shlex
import os

def main():

    kibanaEP= 'http://kibana:5601'

    # import dashboards
    os.chdir("/tmp")
    for file in glob.glob("dashboard_*.json"):
        cmd = "/usr/bin/curl -XPOST %s/api/kibana/dashboards/import -H 'kbn-xsrf:true' -H 'Content-type:application/json' -d @/tmp/%s" % (kibanaEP, file)
        subprocess.check_call(shlex.split(cmd), shell=False)
        print '%s ... dashboard created from %s.' % (cmd, file)
        time.sleep(2)

    # set default index
    cmd = "/usr/bin/curl -v -XPOST -H 'Content-Type: application/json' -H 'kbn-xsrf: true' %s/api/kibana/settings/defaultIndex -d@/tmp/default.json" % kibanaEP
    subprocess.check_call(shlex.split(cmd), shell=False)
    print cmd + ' ... default Index set.'

if __name__ == '__main__':
    main()
