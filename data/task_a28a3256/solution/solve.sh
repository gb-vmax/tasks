#!/bin/bash
set -e
cd /home/user

grep -e 'Failed password' -e 'authentication failure' /home/user/security/audit.log > /home/user/security/failed_logins.report
cat /home/user/security/failed_logins.report
