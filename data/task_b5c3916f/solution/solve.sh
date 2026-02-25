#!/bin/bash
set -e
cd /home/user

(
for srv in ssh ftp http; do
  echo "[$(echo $srv | tr a-z A-Z)]"
  awk -v srv="[$srv]" '
    $0==srv {ins=1; next}
    /^\[.*\]/ {ins=0}
    ins && $2=="=" && $3=="allowed" {
      gsub(/[ \t]*=.*$/, "", $1)
      print $1
    }
  ' /home/user/configs/auth_config.ini | sort
done
) > /home/user/output/audit_user_access.log
mkdir -p /home/user/output
(
for srv in ssh ftp http; do
  echo "[$(echo $srv | tr a-z A-Z)]"
  awk -v srv="[$srv]" '
    $0==srv {ins=1; next}
    /^\[.*\]/ {ins=0}
    ins && $2=="=" && $3=="allowed" {
      gsub(/[ \t]*=.*$/, "", $1)
      print $1
    }
  ' /home/user/configs/auth_config.ini | sort
done
) > /home/user/output/audit_user_access.log
cat /home/user/output/audit_user_access.log
