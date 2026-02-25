#!/bin/bash
set -e
cd /home/user

python3 -c "import csv, json; f=open('/home/user/services/input/services.csv'); r=csv.DictReader(f); data=[{{'service_name': row['service_name'], 'image': row['image'], 'exposed_port': int(row['exposed_port'])}} for row in r]; f.close(); json.dump(data, open('/home/user/services/output/services.json','w'), indent=4)"
python3 -c "import csv, json; f=open('/home/user/services/input/services.csv'); r=csv.DictReader(f); data=[{'service_name': row['service_name'], 'image': row['image'], 'exposed_port': int(row['exposed_port'])} for row in r]; f.close(); json.dump(data, open('/home/user/services/output/services.json','w'), indent=4)"
cat /home/user/services/output/services.json
