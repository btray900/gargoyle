#!/usr/bin/env python3

'''Setup initial env vars for elastic container, pre users'''

import yaml

with open('rc.yaml', 'r') as y:
    g_vars = yaml.load(y)

rc = open('.gargoylerc', 'w')
app_rc = open('env.gargoyle', 'w')

for k, v in g_vars.items():
    environment_key = k.upper()
    rc.write(f'export {environment_key}={v}\n')
    app_rc.write(f'{environment_key}={v}\n')

rc.close()
app_rc.close()
