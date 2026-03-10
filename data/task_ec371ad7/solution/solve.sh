#!/bin/bash
set -e
cd /home/user

cat /home/user/project/deploy.ini
python3 -c "
import configparser

config = configparser.ConfigParser()
config.read('/home/user/project/deploy.ini')

lines = []
for section in config.sections():
    host = config[section]['host']
    port = config[section]['port']
    lines.append(f'[{section}] host={host} port={port}')

with open('/home/user/project/config_summary.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')
"
echo '; summary generated' >> /home/user/project/deploy.ini
cat /home/user/project/config_summary.txt
cat /home/user/project/deploy.ini
