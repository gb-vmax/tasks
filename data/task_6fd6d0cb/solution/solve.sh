#!/bin/bash
set -e
cd /home/user

cat /home/user/deploys/deployment.log
python3 /tmp/gen_report.py
cat > /tmp/report_gen.py /dev/null
python3 -c "
import re
from collections import defaultdict
entries = []
for line in open('/home/user/deploys/deployment.log'):
    line = line.strip()
    if not line: continue
    m = re.match(r'\[(\S+)\] SERVICE=(\S+) VERSION=(\S+) STATUS=(\S+) DURATION=(\d+)s REGION=(\S+)', line)
    if m:
        ts,service,version,status,duration,region = m.groups()
        entries.append({'ts':ts,'service':service,'version':version,'status':status,'duration':int(duration),'region':region})
total=len(entries)
successful=sum(1 for e in entries if e['status']=='DEPLOYED')
failed=total-successful
success_rate=round(successful/total*100,1)
svc=defaultdict(lambda:{'success':0,'total':0,'durations':[]})
for e in entries:
    svc[e['service']]['total']+=1
    svc[e['service']]['durations'].append(e['duration'])
    if e['status']=='DEPLOYED': svc[e['service']]['success']+=1
reg=defaultdict(lambda:{'success':0,'total':0})
for e in entries:
    reg[e['region']]['total']+=1
    if e['status']=='DEPLOYED': reg[e['region']]['success']+=1
slowest=None
fastest=None
for e in entries:
    if slowest is None or e['duration']>=slowest['duration']: slowest=e
    if fastest is None or e['duration']<=fastest['duration']: fastest=e
degraded=[]
for s in sorted(svc.keys()):
    sd=svc[s]
    if sd['success']<sd['total']:
        rate=round(sd['success']/sd['total']*100,1)
        degraded.append((s,rate))
out=[]
out.append('=== DEPLOYMENT HEALTH REPORT ===')
out.append('Generated: 2024-06-10')
out.append('')
out.append('Total deployments: '+str(total))
out.append('Successful: '+str(successful))
out.append('Failed/Rolled back: '+str(failed))
out.append('Overall success rate: '+str(success_rate)+'%')
out.append('')
out.append('=== PER-SERVICE SUMMARY ===')
for s in sorted(svc.keys()):
    sd=svc[s]
    avg=round(sum(sd['durations'])/len(sd['durations']))
    out.append(s+': '+str(sd['success'])+'/'+str(sd['total'])+' succeeded, avg duration '+str(avg)+'s')
out.append('')
out.append('=== REGIONAL BREAKDOWN ===')
for r in sorted(reg.keys()):
    rd=reg[r]
    out.append(r+': '+str(rd['success'])+'/'+str(rd['total'])+' deployments succeeded')
out.append('')
out.append('=== ALERTS ===')
out.append('DEGRADED SERVICES (success rate < 100%):')
if degraded:
    for s,rate in degraded: out.append('  '+s+': '+str(rate)+'% success rate')
else: out.append('  (none)')
out.append('SLOWEST DEPLOYMENT: '+slowest['service']+' v'+slowest['version']+' in '+slowest['region']+' took '+str(slowest['duration'])+'s')
out.append('FASTEST DEPLOYMENT: '+fastest['service']+' v'+fastest['version']+' in '+fastest['region']+' took '+str(fastest['duration'])+'s')
open('/home/user/deploys/deploy_report.txt','w').write('\n'.join(out)+'\n')
print('Done')
"
cat /home/user/deploys/deploy_report.txt
