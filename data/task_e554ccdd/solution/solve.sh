#!/bin/bash
set -e
cd /home/user

ls /home/user/dashboards/ 2>/dev/null || echo "Directory does not exist"
find /home/user/dashboards -type f -o -type l | sort
find /home/user/dashboards/active -type l | sort | xargs -I{} sh -c 'echo "{} -> $(readlink {})"'
cd /home/user/dashboards && \
ln -sf ../../templates/infra/nodes_v3.json active/production/nodes.json && \
ln -sf ../../templates/app/requests_v3.json active/production/requests.json && \
ln -sf ../../templates/db/queries_v2.json active/production/queries.json && \
ln -sf ../../templates/app/latency_v2.json active/staging/latency.json && \
mkdir -p active/development && \
ln -sf ../../templates/infra/nodes_v2.json active/development/nodes.json && \
ln -sf ../../templates/app/latency_v2.json active/development/latency.json && \
ln -sf ../../templates/app/requests_v3.json active/development/requests.json && \
ln -sf ../../templates/db/queries_v1.json active/development/queries.json
cd /home/user/dashboards && \
mv templates/infra/nodes_v1.json archive/nodes_v1.json && \
ln -sf ../../archive/nodes_v1.json templates/infra/nodes_v1.json
cd /home/user/dashboards && python3 -c "
import os

envs = sorted(os.listdir('active'))
lines = ['=== Dashboard Symlink Audit ===']
total = 0

for i, env in enumerate(envs):
    lines.append('')
    lines.append(f'[{env}]')
    env_path = os.path.join('active', env)
    symlinks = sorted(os.listdir(env_path))
    for name in symlinks:
        path = os.path.join(env_path, name)
        if os.path.islink(path):
            target = os.readlink(path)
            lines.append(f'  {name} -> {target}')
            total += 1

lines.append('')
lines.append(f'Total symlinks: {total}')

report = '\n'.join(lines) + '\n'
print(report, end='')
with open('audit_report.txt', 'w') as f:
    f.write(report)
"
echo "=== Verify archive ===" && \
ls -la /home/user/dashboards/templates/infra/nodes_v1.json && \
ls -la /home/user/dashboards/archive/nodes_v1.json && \
echo "" && \
echo "=== Verify all active symlinks ===" && \
find /home/user/dashboards/active -type l | sort | xargs -I{} sh -c 'echo "{} -> $(readlink {})"' && \
echo "" && \
echo "=== Audit report ===" && \
cat /home/user/dashboards/audit_report.txt
