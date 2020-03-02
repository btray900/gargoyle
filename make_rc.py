#!/usr/bin/env python3
#!/usr/bin/env python3

import sys
import random
import string
import os
import yaml

exists = os.path.isfile('.gargoylerc')
if exists:
    print('WARNING: Password file exists, move it to prevent overwriting password file.')
    sys.exit()

with open('./.gargoyle.creds', 'r') as f:
    lines = f.readlines()


with open('rc.yaml', 'r') as y:
    svt_vars = yaml.load(y)

rc = open('.gargoylerc', 'w')
app_rc = open('env.gargoyle', 'w')

for k, v in svt_vars.items():
    environment_key = k.upper()
    rc.write(f'export {environment_key}={v}\n')
    app_rc.write(f'{environment_key}={v}\n')

for line in lines:
    if 'kibana' in line:
        line = line.strip()
        p = line.split('=')
        rc.write('export KIBANA_PW=%s\n' % p[-1].strip())
        app_rc.write('KIBANA_PW=%s\n' % p[-1].strip())

    if 'elastic' in line:
        line = line.strip()
        p = line.split('=')
        rc.write('export ELASTIC_PW=%s\n' % p[-1].strip())
        app_rc.write('ELASTIC_PW=%s\n' % p[-1].strip())


apiPassword = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(20))
rc.write('export API_PW=%s\n' % apiPassword)
app_rc.write('API_PW=%s\n' % apiPassword)

apacheUserPassword = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(20))
rc.write('export APACHE_PW=%s\n' % apacheUserPassword)
app_rc.write('APACHE_PW=%s\n' % apacheUserPassword)

dbUserPassword = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(20))
rc.write('export DB_PW=%s\n' % dbUserPassword)
app_rc.write('DB_PW=%s\n' % dbUserPassword)

dbRootUserPassword = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(20))
rc.write('export DB_ROOT_PW=%s\n' % dbRootUserPassword)
app_rc.write('DB_ROOT_PW=%s\n' % dbRootUserPassword)

rc.close()
app_rc.close()
