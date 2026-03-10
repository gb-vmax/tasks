#!/bin/bash
set -e
cd /home/user

cat /home/user/sshd_config
sed -i 's/^PermitRootLogin yes/PermitRootLogin no/' /home/user/sshd_config && sed -i 's/^PasswordAuthentication yes/PasswordAuthentication no/' /home/user/sshd_config && sed -i 's/^X11Forwarding yes/X11Forwarding no/' /home/user/sshd_config
printf 'SSH Hardening Report\n====================\nPermitRootLogin: yes -> no\nPasswordAuthentication: yes -> no\nX11Forwarding: yes -> no\n' > /home/user/sshd_hardening_report.txt
cat /home/user/sshd_config && echo "---" && cat /home/user/sshd_hardening_report.txt
