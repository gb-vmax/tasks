#!/bin/bash
set -e
cd /home/user

head -20 /home/user/logs/service_errors.csv
wc -l /home/user/logs/service_errors.csv && cat /home/user/logs/service_errors.csv
python3 /home/user/logs/gen_report.py
python3 -c "
import csv,os
from collections import defaultdict
rows=[]
with open('/home/user/logs/service_errors.csv') as f:
    for r in csv.DictReader(f): rows.append(r)
st=defaultdict(int); se=defaultdict(int)
for r in rows:
    st[r['service']]+=1
    if r['level']=='ERROR': se[r['service']]+=1
ebs=[(s,se[s],round(se[s]/st[s]*100,1)) for s in st]
ebs.sort(key=lambda x:(-x[1],x[0]))
ecc=defaultdict(int)
for r in rows:
    if r['level']=='ERROR' and int(r['error_code'])!=0: ecc[int(r['error_code'])]+=1
te=sorted(ecc.items(),key=lambda x:(-x[1],x[0]))[:3]
rt=defaultdict(list)
for r in rows: rt[r['region']].append(int(r['response_time_ms']))
rs=[(rg,round(sum(rt[rg])/len(rt[rg])),max(rt[rg])) for rg in sorted(rt)]
he=defaultdict(int)
for r in rows:
    if r['level']=='ERROR': he[r['timestamp'][11:13]]+=1
hs=sorted(he.items())
sec=defaultdict(list)
for r in rows:
    if r['level']=='ERROR' and int(r['error_code'])!=0: sec[r['service']].append(int(r['error_code']))
crit=[]
for s,codes in sec.items():
    d=set(codes)
    if len(d)>=3:
        cf=defaultdict(int)
        for c in codes: cf[c]+=1
        w=sorted(cf.items(),key=lambda x:(-x[1],-x[0]))[0][0]
        crit.append((s,len(d),w))
crit.sort(key=lambda x:(-x[1],x[0]))
out=['=== SERVICE ERROR REPORT ===','','[ERROR COUNTS BY SERVICE]']
for s,e,p in ebs: out.append('{}: {} errors ({}%)'.format(s,e,p))
out+=['','[TOP ERROR CODES]']
for c,n in te: out.append('{}: {} occurrences'.format(c,n))
out+=['','[RESPONSE TIME BY REGION]']
for rg,a,m in rs: out.append('{}: avg {}ms, max {}ms'.format(rg,a,m))
out+=['','[HOURLY ERROR RATE]']
for h,n in hs: out.append('{}:00 - {} errors'.format(h,n))
out+=['','[CRITICAL SERVICES]']
for s,e,w in crit: out.append('{} - {} unique error codes, worst code: {}'.format(s,e,w))
open('/home/user/logs/error_report.txt','w').write('\n'.join(out)+'\n')
"
cat /home/user/logs/error_report.txt
cat -A /home/user/logs/error_report.txt
