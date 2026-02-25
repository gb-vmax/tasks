#!/bin/bash
set -e
cd /home/user

python3 -c "import csv, json; fin=open('/home/user/legacy_services/services.csv'); fout=open('/home/user/legacy_services/active_services.jsonl','w'); rdr=csv.DictReader(fin); [fout.write(json.dumps({'id':r['service_id'],'name':r['service_name'],'endpoint':f'tcp://{r['legacy_ip']}:{r['port']}','admin':r['owner']})+'\n') for r in rdr if r['state']=='active']; fin.close(); fout.close()"
python3 -c "import csv, json; fin=open('/home/user/legacy_services/services.csv'); fout=open('/home/user/legacy_services/active_services.jsonl','w'); rdr=csv.DictReader(fin); [fout.write(json.dumps({'id':r['service_id'],'name':r['service_name'],'endpoint':'tcp://'+r['legacy_ip']+':'+r['port'],'admin':r['owner']})+'\n') for r in rdr if r['state']=='active']; fin.close(); fout.close()"
total=$(($(wc -l < /home/user/legacy_services/services.csv) - 1)); active=$(wc -l < /home/user/legacy_services/active_services.jsonl); echo "Total services found: $total" > /home/user/legacy_services/transform.log; echo "Total active services exported: $active" >> /home/user/legacy_services/transform.log
cat /home/user/legacy_services/active_services.jsonl /home/user/legacy_services/transform.log
