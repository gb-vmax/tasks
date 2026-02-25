#!/bin/bash
set -e
cd /home/user

bash -c '
cd /home/user/workspace

ok=1

# Specified targets and required perms
p1_target="/home/user/projects/main_project.txt"
p2_target="/home/user/config/settings.conf"
p3_target="/home/user/data/raw_dataset.csv"

p1_link="project_link"
p2_link="config_symlink"
p3_link="data_link"

p1_lp="lrwxrwxrwx"
p2_lp="lrwxrwxrwx"
p3_lp="lrwxrwxrwx"

p1_tp="-rw-------"
p2_tp="-rw-r-----"
p3_tp="-rwxr-x---"

# Function to get permissions (link or target)
plink() { stat -c "%A" -- "$1"; }
ptarget() { stat -Lc "%A" -- "$1"; }

# Check symlink existence and targets
[ -L "$p1_link" ] && [ "$(readlink -- "$p1_link")" = "$p1_target" ] || ok=0
[ -L "$p2_link" ] && [ "$(readlink -- "$p2_link")" = "$p2_target" ] || ok=0
[ -L "$p3_link" ] && [ "$(readlink -- "$p3_link")" = "$p3_target" ] || ok=0

# Check symlink perms
[ "$(plink "$p1_link")" = "$p1_lp" ] || ok=0
[ "$(plink "$p2_link")" = "$p2_lp" ] || ok=0
[ "$(plink "$p3_link")" = "$p3_lp" ] || ok=0

# Check target perms
[ "$(ptarget "$p1_link")" = "$p1_tp" ] || ok=0
[ "$(ptarget "$p2_link")" = "$p2_tp" ] || ok=0
[ "$(ptarget "$p3_link")" = "$p3_tp" ] || ok=0

if [ "$ok" -eq 1 ]; then
  cat > /home/user/audit_report.txt <<EOF
Symbolic Link Audit Report
--------------------------
project_link: EXISTS, points to /home/user/projects/main_project.txt, perms: lrwxrwxrwx, target perms: -rw-------
config_symlink: EXISTS, points to /home/user/config/settings.conf, perms: lrwxrwxrwx, target perms: -rw-r-----
data_link: EXISTS, points to /home/user/data/raw_dataset.csv, perms: lrwxrwxrwx, target perms: -rwxr-x---
EOF
else
  echo "Audit failed: Discrepancy found in symbolic links or permissions." > /home/user/audit_report.txt
fi

cat /home/user/audit_report.txt
'
