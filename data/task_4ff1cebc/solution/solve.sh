#!/bin/bash
set -e
cd /home/user

tar -czf /home/user/diagnostics/diagnostics.tar.gz -C /home/user/logs syslog.txt auth.log kernel.log
tar -tzf /home/user/diagnostics/diagnostics.tar.gz > /home/user/diagnostics/diagnostics_archive_contents.txt
cat /home/user/diagnostics/diagnostics_archive_contents.txt
