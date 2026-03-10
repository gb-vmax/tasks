#!/bin/bash
set -e
cd /home/user

cat /home/user/provisioning/server_spec.json
cat > /home/user/provisioning/solve_provisioning.py << 'EOF'
import json
from scipy.optimize import linprog

# Read the spec
with open('/home/user/provisioning/server_spec.json') as f:
    spec = json.load(f)

budget = spec['budget']
rack_units = spec['rack_units']
servers = spec['servers']

n = len(servers)

# Objective: maximize sum of vcpus * x_i => minimize negative
c = [-s['vcpus'] for s in servers]

# Constraints: budget and rack units (<=)
A_ub = [
    [s['cost'] for s in servers],
    [s['ru'] for s in servers],
]
b_ub = [budget, rack_units]

# Bounds: each x_i >= 0
bounds = [(0, None)] * n

result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

if result.status != 0:
    raise RuntimeError(f"LP failed: {result.message}")

x = result.x
total_vcpus = -result.fun
budget_used = sum(servers[i]['cost'] * x[i] for i in range(n))
ru_used = sum(servers[i]['ru'] * x[i] for i in range(n))

lines = []
lines.append("=== PROVISIONING PLAN ===")
lines.append(f"Budget used: ${budget_used:.2f} of ${budget}")
lines.append(f"Rack units used: {ru_used:.2f} of {rack_units}")
lines.append(f"Total vCPUs: {total_vcpus:.2f}")
lines.append("")
lines.append("Allocation:")
for i, s in enumerate(servers):
    lines.append(f"  {s['name']}: {x[i]:.2f}")

output = "\n".join(lines) + "\n"

with open('/home/user/provisioning/provisioning_plan.txt', 'w') as f:
    f.write(output)

print("Done.")
print(output)
EOF
python3 /home/user/provisioning/solve_provisioning.py
pip install scipy -q
python3 /home/user/provisioning/solve_provisioning.py
cat /home/user/provisioning/provisioning_plan.txt
