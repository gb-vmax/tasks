#!/bin/bash
set -e
cd /home/user

cat /home/user/db_config.ini
python3 -c "
import configparser
config = configparser.ConfigParser()
config.read('/home/user/db_config.ini')
lines = [
    'host=' + config['connection']['host'].strip(),
    'port=' + config['connection']['port'].strip(),
    'max_connections=' + config['performance']['max_connections'].strip(),
    'query_timeout=' + config['performance']['query_timeout'].strip(),
    'slow_query_log=' + config['logging']['slow_query_log'].strip(),
]
with open('/home/user/db_summary.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')
"
cat /home/user/db_summary.txt
wc -l /home/user/db_summary.txt
