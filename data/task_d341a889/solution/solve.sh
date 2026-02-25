#!/bin/bash
set -e
cd /home/user

awk -F, 'NR==1{for(i=1;i<=NF;i++)h[$i]=i} NR>1 && $h["provisioned"]=="no"{printf "{\x22hostname\x22:\x22%s\x22,\x22ip_address\x22:\x22%s\x22,\x22os_type\x22:\x22%s\x22}\n", $h["hostname"], $h["ip_address"], $h["os_type"]}' /home/user/server_inventory.csv | jq -s '.' | jq '.' > /home/user/provision_requests.json
python3 -c "import csv, json; f=open('/home/user/server_inventory.csv'); r=csv.DictReader(f); out=[{'hostname':row['hostname'], 'ip_address':row['ip_address'], 'os_type':row['os_type']} for row in r if row['provisioned']=='no']; json.dump(out, open('/home/user/provision_requests.json','w'), indent=4)"
python3 -c "import csv; rows=[]; fn='/home/user/server_inventory.csv'; f=open(fn); r=csv.DictReader(f); rows=[dict(row, provisioned='yes') if row['provisioned']=='no' else row for row in r]; f.close(); w=open(fn,'w',newline=''); wr=csv.DictWriter(w,fieldnames=r.fieldnames); wr.writeheader(); wr.writerows(rows); w.close()"
python3 -c "import json, datetime; reqs=json.load(open('/home/user/provision_requests.json')); now=datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]'); with open('/home/user/provisioning_audit.log','w') as log: [log.write(f'{now} Changed server {req[\"hostname\"]} provisioning status from \x27no\x27 to \x27yes\x27\n') for req in reqs]"
python3 -c "import json, datetime; reqs=json.load(open('/home/user/provision_requests.json')); log=open('/home/user/provisioning_audit.log','w'); [log.write('[%s] Changed server %s provisioning status from \\'no\\' to \\'yes\\'\n' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), req['hostname'])) for req in reqs]; log.close()"
head -20 /home/user/provision_requests.json /home/user/server_inventory.csv /home/user/provisioning_audit.log
