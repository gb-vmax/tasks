#!/bin/bash
set -e
cd /home/user

ln -sf /home/user/dashboards/prod_dashboard.json /home/user/active_dashboard.json && ln -sf /home/user/dashboards/prod_dashboard.json /home/user/envs/prod/dashboard.json && ln -sf /home/user/dashboards/staging_dashboard.json /home/user/envs/staging/dashboard.json && printf "/home/user/active_dashboard.json\t/home/user/dashboards/prod_dashboard.json\n/home/user/envs/prod/dashboard.json\t/home/user/dashboards/prod_dashboard.json\n/home/user/envs/staging/dashboard.json\t/home/user/dashboards/staging_dashboard.json\n" > /home/user/dashboard_symlink_check.log
