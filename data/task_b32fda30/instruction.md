I'm working on a Kubernetes operator that manages pod scheduling across nodes. The operator needs to decide how many replicas of each workload to run, subject to node resource constraints. I've modeled this as a linear program and need you to solve it using Python (scipy or any available LP solver) and write the results to a specific output file.

The resource constraints and workload definitions are already saved in `/home/user/k8s_optimizer/workloads.json`. This file describes available node capacity and workload resource requirements.

Here's what the operator needs to do:

**The Optimization Problem:**

We have 3 workloads: `api-server`, `worker`, and `cache`. We want to **maximize** the total throughput score, where:
- Each replica of `api-server` contributes **5** throughput units
- Each replica of `worker` contributes **8** throughput units
- Each replica of `cache` contributes **3** throughput units

Subject to these node resource constraints (total across all replicas):
- **CPU constraint**: `api-server` uses 2 CPU units/replica, `worker` uses 4 CPU units/replica, `cache` uses 1 CPU unit/replica. Total CPU available: **24 units**
- **Memory constraint**: `api-server` uses 3 GB/replica, `worker` uses 2 GB/replica, `cache` uses 4 GB/replica. Total memory available: **24 GB**
- **Pod slot constraint**: total replicas across all workloads cannot exceed **8** (max pods schedulable on the cluster)

Each workload must have at least **1 replica** and at most **6 replicas**. The number of replicas must be a **whole number** (integer).

**What I need you to do:**

1. Write a Python script at `/home/user/k8s_optimizer/solve.py` that reads `/home/user/k8s_optimizer/workloads.json`, solves this integer linear program (ILP), and writes the results to `/home/user/k8s_optimizer/schedule.txt`.

2. Run the script to produce `/home/user/k8s_optimizer/schedule.txt`.

The output file `/home/user/k8s_optimizer/schedule.txt` must contain exactly the following format (with the correct computed values substituted):

```
=== Kubernetes Operator Schedule ===
api-server: <N> replicas
worker: <N> replicas
cache: <N> replicas
Total throughput: <N>
Status: OPTIMAL
```

Where each `<N>` is an integer. There should be no trailing spaces on any line. The file should end with a single newline character after the `Status: OPTIMAL` line.

The `/home/user/k8s_optimizer/workloads.json` file already exists and contains the problem data — your script must read from it (not hardcode the numbers), but you can inspect its contents to understand the structure.
