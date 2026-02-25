#!/bin/bash
set -e
cd /home/user

awk -F= '
/^\[/ { if (name && status == "release") print name; name=""; status="" }
$1 ~ /^name$/ { gsub(/^ +| +$/, "", $2); name=$2 }
$1 ~ /^status$/ { gsub(/^ +| +$/, "", $2); status=$2 }
END { if (name && status == "release") print name }
' /home/user/projects/build_config/artifacts.ini
