FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/k8s_optimizer

cat > /home/user/k8s_optimizer/workloads.json << 'EOF'
{
  "workloads": [
    {"name": "api-server", "cpu": 2, "memory": 3, "throughput": 5},
    {"name": "worker",     "cpu": 4, "memory": 2, "throughput": 8},
    {"name": "cache",      "cpu": 1, "memory": 4, "throughput": 3}
  ],
  "cluster": {
    "total_cpu": 24,
    "total_memory": 24,
    "max_pods": 8
  },
  "replica_bounds": {
    "min": 1,
    "max": 6
  }
}
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
