#!/bin/bash
set -e
cd /home/user

cat /home/user/incidents/raw_incidents.json
python3 -c "
import json, csv, io

with open('/home/user/incidents/raw_incidents.json') as f:
    incidents = json.load(f)

filtered = [inc for inc in incidents if inc['severity'] in ('critical', 'high') and inc['status'] in ('open', 'investigating')]

sev_order = {'critical': 0, 'high': 1}
filtered.sort(key=lambda x: (sev_order[x['severity']], x['opened_at']))

buf = io.StringIO()
writer = csv.writer(buf, lineterminator='\n')
writer.writerow(['id', 'severity', 'service', 'title', 'opened_at'])
for inc in filtered:
    writer.writerow([inc['id'], inc['severity'], inc['service'], inc['title'], inc['opened_at']])

content = buf.getvalue()
with open('/home/user/incidents/triage.csv', 'w', newline='') as f:
    f.write(content)
print(repr(content))
"
cat /home/user/incidents/triage.csv
xxd /home/user/incidents/triage.csv | tail -3
od -c /home/user/incidents/triage.csv | tail -3
