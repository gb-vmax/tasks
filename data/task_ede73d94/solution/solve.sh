#!/bin/bash
set -e
cd /home/user

ls -l /home/user/dashboards/
chmod 640 /home/user/dashboards/grafana_main.json /home/user/dashboards/alerts_config.json /home/user/dashboards/datasources.cfg
chown :observer /home/user/dashboards/grafana_main.json /home/user/dashboards/alerts_config.json /home/user/dashboards/datasources.cfg
ls -l /home/user/dashboards/
