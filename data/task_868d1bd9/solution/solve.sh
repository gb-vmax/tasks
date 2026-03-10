#!/bin/bash
set -e
cd /home/user

cat /home/user/pipeline/build.ini
python3 -c "
import configparser
config = configparser.ConfigParser()
config.read('/home/user/pipeline/build.ini')

lines = [
    'app_name=' + config['project']['app_name'].strip(),
    'version_name=' + config['project']['version_name'].strip(),
    'version_code=' + config['project']['version_code'].strip(),
    'build_type=' + config['android']['build_type'].strip(),
    'min_sdk=' + config['android']['min_sdk'].strip(),
    'target_sdk=' + config['android']['target_sdk'].strip(),
    'scheme=' + config['ios']['scheme'].strip(),
    'deployment_target=' + config['ios']['deployment_target'].strip(),
]

with open('/home/user/pipeline/build_summary.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')
"
cat /home/user/pipeline/build_summary.txt
