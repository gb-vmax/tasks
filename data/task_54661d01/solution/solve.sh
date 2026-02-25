#!/bin/bash
set -e
cd /home/user

echo "Cloud cost savings for Q2: \$18,430" > /home/user/cloud_cost_report_Q2.txt
gpg --batch --passphrase '' --quick-gen-key "Jane Finops <jane.finops@example.com>" default default never
gpg --batch --yes --detach-sign --local-user "Jane Finops <jane.finops@example.com>" -o /home/user/cloud_cost_report_Q2.txt.sig /home/user/cloud_cost_report_Q2.txt
gpg --batch --yes --output /home/user/cloud_cost_report_Q2.txt.gpg --recipient "Jane Finops <jane.finops@example.com>" --encrypt /home/user/cloud_cost_report_Q2.txt
(gpg --verify /home/user/cloud_cost_report_Q2.txt.sig /home/user/cloud_cost_report_Q2.txt 2>&1 | grep -q "Good signature" && status="GOOD" || status="BAD") && echo "[$(date '+%Y-%m-%d %H:%M:%S')] Verification status: $status signature for cloud_cost_report_Q2.txt" > /home/user/cloud_cost_report_verification.log
cat /home/user/cloud_cost_report_verification.log
bash -c 'if gpg --verify /home/user/cloud_cost_report_Q2.txt.sig /home/user/cloud_cost_report_Q2.txt 2>&1 | grep -q "Good signature"; then status=GOOD; else status=BAD; fi; echo "[$(date \"+%Y-%m-%d %H:%M:%S\")] Verification status: $status signature for cloud_cost_report_Q2.txt" > /home/user/cloud_cost_report_verification.log'
bash -c 'if gpg --verify /home/user/cloud_cost_report_Q2.txt.sig /home/user/cloud_cost_report_Q2.txt 2>&1 | grep -q "Good signature"; then status=GOOD; else status=BAD; fi; echo "[$(date \"+%Y-%m-%d %H:%M:%S\")] Verification status: $status signature for cloud_cost_report_Q2.txt" > /home/user/cloud_cost_report_verification.log'
bash -c 'timestamp=$(date "+%Y-%m-%d %H:%M:%S"); if gpg --verify /home/user/cloud_cost_report_Q2.txt.sig /home/user/cloud_cost_report_Q2.txt 2>&1 | grep -q "Good signature"; then status=GOOD; else status=BAD; fi; echo "[$timestamp] Verification status: $status signature for cloud_cost_report_Q2.txt" > /home/user/cloud_cost_report_verification.log'
cat /home/user/cloud_cost_report_verification.log
