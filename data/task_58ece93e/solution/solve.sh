#!/bin/bash
set -e
cd /home/user

id alice && getent group devteam && ls -la /home/user/projects/webapp/config.cfg && ls -la /home/user/tickets/ 2>/dev/null || echo "tickets dir may not exist"
usermod -aG devteam alice
chmod 0640 /home/user/projects/webapp/config.cfg
printf 'Ticket: 042\nStatus: resolved\nUser: alice\nGroup added: devteam\nConfig file: /home/user/projects/webapp/config.cfg\nConfig permissions: 640\n' > /home/user/tickets/ticket_042.txt
id alice && getent group devteam && ls -la /home/user/projects/webapp/config.cfg && cat /home/user/tickets/ticket_042.txt
