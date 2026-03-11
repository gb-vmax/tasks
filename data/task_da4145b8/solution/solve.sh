#!/bin/bash
set -e
cd /home/user

cat /home/user/config_changes.log
awk '
BEGIN {
    total=0; success=0; failure=0
}
{
    total++
    match($0, /USER=([^ ]+)/, u)
    match($0, /COMPONENT=([^ ]+)/, c)
    match($0, /STATUS=([^ ]+)/, s)
    user = u[1]; comp = c[1]; status = s[1]
    users[user]++
    comps[comp]++
    if (status == "success") success++
    else failure++
}
END {
    printf "CONFIG CHANGE REPORT\n"
    printf "====================\n"
    printf "Total changes: %d\n", total
    printf "Successful changes: %d\n", success
    printf "Failed changes: %d\n", failure
    printf "\nChanges by user:\n"
    n = asorti(users, sorted_users)
    for (i = 1; i <= n; i++) {
        printf "  %s: %d\n", sorted_users[i], users[sorted_users[i]]
    }
    printf "\nChanges by component:\n"
    m = asorti(comps, sorted_comps)
    for (i = 1; i <= m; i++) {
        if (i < m)
            printf "  %s: %d\n", sorted_comps[i], comps[sorted_comps[i]]
        else
            printf "  %s: %d", sorted_comps[i], comps[sorted_comps[i]]
    }
}
' /home/user/config_changes.log > /home/user/config_report.txt
gawk '
BEGIN {
    total=0; success=0; failure=0
}
{
    total++
    match($0, /USER=([^ ]+)/, u)
    match($0, /COMPONENT=([^ ]+)/, c)
    match($0, /STATUS=([^ ]+)/, s)
    user = u[1]; comp = c[1]; status = s[1]
    users[user]++
    comps[comp]++
    if (status == "success") success++
    else failure++
}
END {
    printf "CONFIG CHANGE REPORT\n"
    printf "====================\n"
    printf "Total changes: %d\n", total
    printf "Successful changes: %d\n", success
    printf "Failed changes: %d\n", failure
    printf "\nChanges by user:\n"
    n = asorti(users, sorted_users)
    for (i = 1; i <= n; i++) {
        printf "  %s: %d\n", sorted_users[i], users[sorted_users[i]]
    }
    printf "\nChanges by component:\n"
    m = asorti(comps, sorted_comps)
    for (i = 1; i <= m; i++) {
        if (i < m)
            printf "  %s: %d\n", sorted_comps[i], comps[sorted_comps[i]]
        else
            printf "  %s: %d", sorted_comps[i], comps[sorted_comps[i]]
    }
}
' /home/user/config_changes.log > /home/user/config_report.txt
python3 - << 'EOF'
import re
from collections import defaultdict

users = defaultdict(int)
comps = defaultdict(int)
total = 0
success = 0
failure = 0

with open('/home/user/config_changes.log') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += 1
        user = re.search(r'USER=(\S+)', line).group(1)
        comp = re.search(r'COMPONENT=(\S+)', line).group(1)
        status = re.search(r'STATUS=(\S+)', line).group(1)
        users[user] += 1
        comps[comp] += 1
        if status == 'success':
            success += 1
        else:
            failure += 1

sorted_users = sorted(users.keys())
sorted_comps = sorted(comps.keys())

lines = []
lines.append("CONFIG CHANGE REPORT")
lines.append("====================")
lines.append(f"Total changes: {total}")
lines.append(f"Successful changes: {success}")
lines.append(f"Failed changes: {failure}")
lines.append("")
lines.append("Changes by user:")
for u in sorted_users:
    lines.append(f"  {u}: {users[u]}")
lines.append("")
lines.append("Changes by component:")
comp_lines = [f"  {c}: {comps[c]}" for c in sorted_comps]

output = "\n".join(lines) + "\n" + "\n".join(comp_lines)

with open('/home/user/config_report.txt', 'w') as f:
    f.write(output)

print("Done")
EOF
cat /home/user/config_report.txt
