#!/bin/bash
set -e
cd /home/user

cat /home/user/pipeline/.env
grep '^CI_' /home/user/pipeline/.env | awk -F'=' '{ name=$1; value=substr($0, index($0,"=")+1); if (tolower(name) ~ /secret|token|password/) { print name "=****" } else { print name "=" value } }' | sort > /home/user/pipeline/ci_audit.txt
cat /home/user/pipeline/ci_audit.txt
