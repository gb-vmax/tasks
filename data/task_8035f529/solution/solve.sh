#!/bin/bash
# Ground truth reference (not an executable solution):
#
# Before the task starts, the following files exist:
# 
# /home/user/cloud_costs.csv (with LF line endings):
# service_name,usage_hours,cost_usd
# Compute-Engine,720,105.60
# Cloud-SQL,500,175.00
# Object-Storage,1200,80.00
# Cloud-Firewall,400,40.00
# BigQuery,90,54.00
# Kubernetes-Engine,300,90.00
# Content-Delivery,150,20.00
# 
# /home/user/services_to_optimize.json:
# [
#     "Cloud-SQL",
#     "Kubernetes-Engine",
#     "Compute-Engine",
#     "BigQuery"
# ]
# 
# Once the agent finishes, the following file should exist:
# 
# /home/user/optimized_costs_report.csv (with LF line endings and no trailing blank lines):
# 
# service_name,usage_hours,cost_usd,cost_per_hour
# BigQuery,90,54.00,0.6000
# Cloud-SQL,500,175.00,0.3500
# Kubernetes-Engine,300,90.00,0.3000
# Compute-Engine,720,105.60,0.1467
# 
# The agent should only display the contents of /home/user/optimized_costs_report.csv, and nothing else, to the terminal as the final step.

echo 'No automated solution provided.'
