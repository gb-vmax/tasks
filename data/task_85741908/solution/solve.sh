#!/bin/bash
set -e
cd /home/user

groupadd devops
useradd -m -d /home/alice -s /bin/bash -g devops alice
chmod 700 /home/alice
install -d -m 770 -o alice -g devops /home/alice/projects
echo -e "SECURITY NOTICE:\nAll access to this system is monitored." > /home/alice/security_notice.txt && chown alice:devops /home/alice/security_notice.txt && chmod 600 /home/alice/security_notice.txt
printf "[STEP 1] Group 'devops' created.\n[STEP 2] User 'alice' created with group 'devops', home '/home/alice', shell '/bin/bash'.\n[STEP 3] Directory '/home/alice' permissions set to 700.\n[STEP 4] Directory '/home/alice/projects' created, permissions set to 770, group 'devops'.\n[STEP 5] File '/home/alice/security_notice.txt' created with owner-only permissions (600).\n" > /home/user/hardening_log.txt
cat /home/alice/security_notice.txt
cat /home/user/hardening_log.txt
