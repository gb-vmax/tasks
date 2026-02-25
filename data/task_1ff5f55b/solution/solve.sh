#!/bin/bash
set -euo pipefail

# Create symlinks in /home/user pointing to tools
ln -sf /home/user/tools/ping_test.sh /home/user/pingtest
ln -sf /home/user/tools/ping_output.log /home/user/pinglog

# Create symlink report
printf '%s\n%s\n' \
  'pingtest -> /home/user/tools/ping_test.sh' \
  'pinglog -> /home/user/tools/ping_output.log' \
  > /home/user/symlink_report.log
