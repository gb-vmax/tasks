#!/bin/bash
set -e
cd /home/user

cd /home/user/uptime_check && diff -u status_page_v1.html status_page_v2.html > status_page.patch
cp /home/user/uptime_check/status_page_v1.html /home/user/uptime_check/status_page_v1_backup.html
cd /home/user/uptime_check && patch status_page_v1.html status_page.patch
cd /home/user/uptime_check && if [ -z "$(diff -u status_page_v1.html status_page_v2.html)" ]; then echo "Patching successful: Files are identical after patch application." > patch_verification.log; else diff -u status_page_v1.html status_page_v2.html > patch_verification.log; fi
