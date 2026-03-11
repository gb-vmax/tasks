#!/bin/bash
set -e
cd /home/user

ls -la /home/user/provisioning/
cat /home/user/provisioning/provision.sh
cat /home/user/provisioning/env.conf
chmod +x /home/user/provisioning/provision.sh && /home/user/provisioning/provision.sh /home/user/provisioning/env.conf > /home/user/provisioning/run.log; echo $?
cat /home/user/provisioning/run.log
N=$(wc -l < /home/user/provisioning/run.log)
M=$(grep -c '^\[DONE\]' /home/user/provisioning/run.log)
{
  printf '=== PROVISIONING REPORT ===\n'
  printf 'Config: /home/user/provisioning/env.conf\n'
  printf 'Exit code: 0\n'
  printf 'Lines logged: %s\n' "$N"
  printf 'Services provisioned: %s\n' "$M"
  printf '\n'
  printf '--- LOG ---\n'
  cat /home/user/provisioning/run.log
} > /home/user/provisioning/report.txt
N=$(wc -l < /home/user/provisioning/run.log)
M=$(grep -c '^\[DONE\]' /home/user/provisioning/run.log)
{
  echo '=== PROVISIONING REPORT ==='
  echo 'Config: /home/user/provisioning/env.conf'
  echo 'Exit code: 0'
  echo "Lines logged: $N"
  echo "Services provisioned: $M"
  echo ''
  echo '--- LOG ---'
  cat /home/user/provisioning/run.log
} > /home/user/provisioning/report.txt
cat /home/user/provisioning/report.txt
