#!/bin/bash
set -e
cd /home/user

ls /home/user/monitoring/
cat /home/user/monitoring/cpu_mem.csv
cat /home/user/monitoring/disk_usage.txt
cat /home/user/monitoring/processes.log
python3 /home/user/monitoring/gen_report.py
printf '%s\n' "import csv" "with open('/home/user/monitoring/cpu_mem.csv') as f:" "    rows=list(csv.DictReader(f))" > /home/user/monitoring/gen_report.py && echo "Script started"
cat > /home/user/monitoring/gen_report.py << 'EOF'
import csv

with open('/home/user/monitoring/cpu_mem.csv') as f:
    rows = list(csv.DictReader(f))
n = len(rows)
cpus = [float(r['cpu_percent']) for r in rows]
mems = [float(r['mem_used_mb'])/float(r['mem_total_mb'])*100 for r in rows]
cpu_avg = round(sum(cpus)/n, 1)
cpu_max = round(max(cpus), 1)
mem_avg = round(sum(mems)/n, 1)
mem_peak = round(max(mems), 1)
disk = []
with open('/home/user/monitoring/disk_usage.txt') as f:
    for line in f:
        p = line.strip().split()
        if p:
            u, t = float(p[1]), float(p[2])
            disk.append((p[0], u, t, round(u/t*100, 1)))
disk.sort()
procs = [l.rstrip() for l in open('/home/user/monitoring/processes.log') if l.strip()]
total_snap = len(procs)
names, zombies, top_v, top_n = set(), 0, -1.0, ''
for l in procs:
    p = l[18:].strip().split()
    names.add(p[0])
    if p[2] == 'zombie':
        zombies += 1
    if float(p[3]) > top_v:
        top_v, top_n = float(p[3]), p[0]
top_v = round(top_v, 1)
EOF
echo "part1 done"
cat >> /home/user/monitoring/gen_report.py << 'EOF'
alerts = []
if cpu_avg > 75.0:
    alerts.append('WARN: High average CPU usage (' + str(cpu_avg) + '%)')
if cpu_max > 90.0:
    alerts.append('WARN: CPU spike detected (' + str(cpu_max) + '%)')
for m, u, t, pc in disk:
    if pc >= 80.0:
        alerts.append('WARN: Disk ' + m + ' at ' + str(pc) + '% capacity')
if zombies > 0:
    alerts.append('WARN: ' + str(zombies) + ' zombie process(es) detected')
def fn(v):
    return str(int(v)) if v == int(v) else str(v)
out = []
out.append('=== SYSTEM HEALTH REPORT ===')
out.append('')
out.append('-- CPU & MEMORY --')
out.append('Samples: ' + str(n))
out.append('CPU avg: ' + str(cpu_avg) + '%')
out.append('CPU max: ' + str(cpu_max) + '%')
out.append('Memory avg usage: ' + str(mem_avg) + '%')
out.append('Memory peak usage: ' + str(mem_peak) + '%')
out.append('')
out.append('-- DISK USAGE --')
for m, u, t, pc in disk:
    out.append(m + ': ' + fn(u) + 'GB / ' + fn(t) + 'GB (' + str(pc) + '%)')
out.append('')
out.append('-- PROCESS SUMMARY --')
out.append('Total snapshots: ' + str(total_snap))
out.append('Unique processes: ' + str(len(names)))
out.append('Zombie processes: ' + str(zombies))
out.append('Top CPU process: ' + top_n + ' (' + str(top_v) + '%)')
out.append('')
out.append('-- ALERTS --')
if alerts:
    out.extend(alerts)
else:
    out.append('No alerts.')
with open('/home/user/monitoring/system_health_report.txt', 'w') as f:
    f.write('\n'.join(out) + '\n')
EOF
echo "part2 done"
python3 /home/user/monitoring/gen_report.py && cat /home/user/monitoring/system_health_report.txt
