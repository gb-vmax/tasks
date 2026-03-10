#!/bin/bash
set -e
cd /home/user

cat /home/user/configs/app.conf.v1
cat /home/user/configs/app.conf.v2
python3 - <<'EOF'
v1_path = "/home/user/configs/app.conf.v1"
v2_path = "/home/user/configs/app.conf.v2"
out_path = "/home/user/configs/changes.txt"

with open(v1_path) as f:
    v1_lines = [line.rstrip('\n') for line in f.readlines()]

with open(v2_path) as f:
    v2_lines = [line.rstrip('\n') for line in f.readlines()]

v2_set = set(v2_lines)
v1_set = set(v1_lines)

removed = [l for l in v1_lines if l not in v2_set]
added = [l for l in v2_lines if l not in v1_set]

total = len(removed) + len(added)

with open(out_path, 'w') as f:
    f.write("CONFIG CHANGE REPORT\n")
    f.write("====================\n")
    f.write("REMOVED:\n")
    for line in removed:
        f.write(f"  - {line}\n")
    f.write("ADDED:\n")
    for line in added:
        f.write(f"  - {line}\n")
    f.write("====================\n")
    f.write(f"Total changes: {total}\n")

print("Done.")
EOF
cat /home/user/configs/changes.txt
