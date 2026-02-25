#!/bin/bash
set -e
cd /home/user

python3 -c "
import configparser
import csv
from collections import OrderedDict

ini = '/home/user/server_config/monitoring.ini'
csvfile = '/home/user/server_config/active_servers.csv'
config = configparser.ConfigParser()
config.optionxform = str
config.read(ini)
with open(csvfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['hostname','ip','interval'])
    for section in config.sections():
        if not section.startswith('server_'):
            continue
        keys = config[section]
        required = ['hostname','ip','enabled','interval']
        if not all(k in keys for k in required):
            continue
        if str(keys['enabled']).strip().lower() == 'true':
            writer.writerow([keys['hostname'], keys['ip'], keys['interval']])
"
cat /home/user/server_config/active_servers.csv
