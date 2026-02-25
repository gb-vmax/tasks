#!/bin/bash
set -e
cd /home/user

if command -v apt >/dev/null 2>&1; then status=$(dpkg -l | grep -qw traceroute && echo "yes" || echo "no"); elif command -v rpm >/dev/null 2>&1; then status=$(rpm -q traceroute >/dev/null 2>&1 && echo "yes" || echo "no"); elif command -v dnf >/dev/null 2>&1; then status=$(dnf list installed traceroute >/dev/null 2>&1 && echo "yes" || echo "no"); else status="no"; fi; echo "Installed: $status" > /home/user/traceroute_status.log
cat /home/user/traceroute_status.log
