#!/usr/bin/env python3

import sys
import random
import string
import os

exists = os.path.isfile('.gargoylerc')
if exists:
    print('WARNING: Password file exists, move it to prevent overwriting password file.')
    sys.exit()

with open('./.gargoyle.creds', 'r') as f:
    lines = f.readlines()

rc = open('.gargoylerc', 'w')

for line in lines:
    if 'kibana' in line:
        line = line.strip()
        p = line.split('=')
        rc.write('export KIBANA_USER=kibana\n')
        rc.write('export KIBANA_PW=%s\n' % p[-1].strip())

    if 'elastic' in line:
        line = line.strip()
        p = line.split('=')
        rc.write('export ELASTIC_USER=elastic\n')
        rc.write('export ELASTIC_PW=%s\n' % p[-1].strip())

apiPassword = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(20))

rc.write('export API_USER=gargoyle\n')
rc.write('export API_PW=%s\n' % apiPassword)

dbUserPassword = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(20))

rc.write('export DB_USER=osg\n')
rc.write('export DB_PW=%s\n' % dbUserPassword)

dbRootUserPassword = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(20))

rc.write('export DB_ROOT_USER=root\n')
rc.write('export DB_ROOT_PW=%s\n' % dbRootUserPassword)

rc.close()
