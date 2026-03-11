#!/bin/bash
set -e
cd /home/user

cat /home/user/app/config.ini
mkdir -p /home/user/diagnostics
python3 -c "
import configparser
config = configparser.ConfigParser()
config.read('/home/user/app/config.ini')

lines = [
    '=== DIAGNOSTICS REPORT ===',
    'Host: ' + config['database']['host'],
    'Port: ' + config['database']['port'],
    'Log Level: ' + config['logging']['level'],
    'Log File: ' + config['logging']['file'],
    'Max Workers: ' + config['server']['max_workers'],
    'Debug Mode: ' + config['server']['debug'],
]

with open('/home/user/diagnostics/report.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')
"
cat /home/user/diagnostics/report.txt
wc -l /home/user/diagnostics/report.txt
