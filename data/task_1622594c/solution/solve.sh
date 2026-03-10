#!/bin/bash
set -e
cd /home/user

ls /home/user/incident/logs/
tar -czf /home/user/incident/incident_errors.tar.gz -C /home/user/incident logs/app.error logs/db.error logs/nginx.error
tar -tvf /home/user/incident/incident_errors.tar.gz > /home/user/incident/archive_manifest.txt
cat /home/user/incident/archive_manifest.txt
ls -lh /home/user/incident/incident_errors.tar.gz && wc -l /home/user/incident/archive_manifest.txt
