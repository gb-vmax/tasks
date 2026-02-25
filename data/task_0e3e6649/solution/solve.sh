#!/bin/bash
set -euo pipefail

# Extract Process (column 2) and CPU% (column 5) from app_profile.csv
awk -F',' 'BEGIN{OFS=","} {print $2,$5}' /home/user/app_profile.csv > /home/user/profile_summary.csv
