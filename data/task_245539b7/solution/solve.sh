#!/bin/bash
set -e
cd /home/user

cat /home/user/artifacts/inventory.psv
cat /home/user/artifacts/repo_ids.txt
paste -d'|' /home/user/artifacts/repo_ids.txt <(cut -d'|' -f1,4,5,6 /home/user/artifacts/inventory.psv) > /home/user/artifacts/report.psv
cat /home/user/artifacts/report.psv
