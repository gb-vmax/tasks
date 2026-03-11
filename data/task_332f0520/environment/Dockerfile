FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/capacity

cat > /home/user/capacity/server_metrics.csv << 'EOF'
hostname,cpu_percent,mem_percent,disk_percent
web01,45.2,62.1,30.0
web02,88.5,77.3,55.2
web03,72.0,91.4,48.7
db01,91.3,85.6,78.1
db02,55.8,43.2,61.0
cache01,23.1,38.9,22.4
cache02,82.7,55.0,34.6
worker01,67.4,88.2,41.3
EOF

cat > /home/user/capacity/analyze_usage.py << 'EOF'
import sys
import csv

def main():
    path = sys.argv[1]
    rows = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({
                'hostname': row['hostname'],
                'cpu': float(row['cpu_percent']),
                'mem': float(row['mem_percent']),
                'disk': float(row['disk_percent']),
            })

    hosts = len(rows)
    cpu_avg = sum(r['cpu'] for r in rows) / hosts
    mem_avg = sum(r['mem'] for r in rows) / hosts
    disk_avg = sum(r['disk'] for r in rows) / hosts

    high_cpu = [r['hostname'] for r in rows if r['cpu'] > 80]
    high_mem = [r['hostname'] for r in rows if r['mem'] > 80]

    print(f"Hosts analyzed: {hosts}")
    print(f"Average CPU usage: {cpu_avg:.1f}%")
    print(f"Average MEM usage: {mem_avg:.1f}%")
    print(f"Average DISK usage: {disk_avg:.1f}%")
    print(f"High CPU hosts (>80%): {', '.join(high_cpu) if high_cpu else 'none'}")
    print(f"High MEM hosts (>80%): {', '.join(high_mem) if high_mem else 'none'}")

if __name__ == '__main__':
    main()
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
