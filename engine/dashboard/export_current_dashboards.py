#!/usr/bin/env python

import json
import subprocess
import shlex
import time

cmd = 'curl -s -XGET http://kibana:5601/api/saved_objects/_find?type=dashboard'
o = subprocess.check_output(shlex.split(cmd), shell=False)
data = json.loads(o)
url = 'http://kibana:5601/api/kibana/dashboards/export'
time.sleep(.5)
for i in data['saved_objects']:
    title = i['attributes']['title']
    title = title.replace(' ','-')
    file = 'dashboard_%s.json' % title
    id = i['id']
    cmd1 = 'cp ./%s ./old.%s' % (file, file)
    subprocess.call(shlex.split(cmd1), shell=False)
    time.sleep(.5)
    cmd2 = 'curl -s -XGET %s?dashboard=%s -o ./%s' % (url, id, file)
    subprocess.check_output(shlex.split(cmd2), shell=False)
    time.sleep(.5)
    print 'Export done for %s:%s' % (id, file)
