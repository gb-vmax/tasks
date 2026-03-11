#!/bin/bash
set -e
cd /home/user

cat /home/user/edge/device_master.ini
grep -c '^\s*[^;#\[]\S*\s*=' /home/user/edge/device_master.ini
python3 -c "
import configparser

config = configparser.ConfigParser()
config.read('/home/user/edge/device_master.ini')

lines = [
    'DEVICE_ID='       + config['device']['id'],
    'FIRMWARE='        + config['device']['firmware_version'],
    'MQTT_HOST='       + config['network']['broker_host'],
    'MQTT_PORT='       + config['network']['broker_port'],
    'POLL_INTERVAL='   + config['sensors']['poll_interval_sec'],
    'TEMP_MAX='        + config['thresholds']['temp_max_celsius'],
    'BATTERY_MIN='     + config['thresholds']['battery_min_pct'],
    'TOTAL_KEYS=16',
]

with open('/home/user/edge/deploy_summary.conf', 'w') as f:
    f.write('\n'.join(lines))
"
cat /home/user/edge/deploy_summary.conf
wc -l /home/user/edge/deploy_summary.conf && xxd /home/user/edge/deploy_summary.conf | tail -3
echo "" >> /home/user/edge/deploy_summary.conf && wc -l /home/user/edge/deploy_summary.conf
cat -A /home/user/edge/deploy_summary.conf
wc -l /home/user/edge/deploy_summary.conf && cat /home/user/edge/deploy_summary.conf
