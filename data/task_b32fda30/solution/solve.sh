#!/bin/bash
set -e
cd /home/user

cat /home/user/k8s_optimizer/workloads.json
cat > /home/user/k8s_optimizer/solve.py << 'SCRIPT'
import json
from itertools import product

with open('/home/user/k8s_optimizer/workloads.json', 'r') as f:
    data = json.load(f)

workloads = data['workloads']
cluster = data['cluster']
bounds = data['replica_bounds']

total_cpu = cluster['total_cpu']
total_memory = cluster['total_memory']
max_pods = cluster['max_pods']
min_rep = bounds['min']
max_rep = bounds['max']

names = [w['name'] for w in workloads]
cpus = [w['cpu'] for w in workloads]
mems = [w['memory'] for w in workloads]
thrs = [w['throughput'] for w in workloads]

best_throughput = -1
best_solution = None

for replicas in product(range(min_rep, max_rep + 1), repeat=len(workloads)):
    cpu_used = sum(replicas[i] * cpus[i] for i in range(len(workloads)))
    mem_used = sum(replicas[i] * mems[i] for i in range(len(workloads)))
    pods_used = sum(replicas)
    if cpu_used <= total_cpu and mem_used <= total_memory and pods_used <= max_pods:
        throughput = sum(replicas[i] * thrs[i] for i in range(len(workloads)))
        if throughput > best_throughput:
            best_throughput = throughput
            best_solution = replicas

lines = [
    "=== Kubernetes Operator Schedule ===",
    "api-server: {} replicas".format(best_solution[0]),
    "worker: {} replicas".format(best_solution[1]),
    "cache: {} replicas".format(best_solution[2]),
    "Total throughput: {}".format(best_throughput),
    "Status: OPTIMAL",
]

with open('/home/user/k8s_optimizer/schedule.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')

print("Done. Solution:", best_solution, "Throughput:", best_throughput)
SCRIPT
python3 /home/user/k8s_optimizer/solve.py
cat /home/user/k8s_optimizer/schedule.txt
