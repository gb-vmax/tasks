#!/bin/bash
# Ground truth reference (not an executable solution):
#
# Directory structure before the task begins:
# /home/user/projects/resmon/
#     ├── CHANGELOG.md
#     ├── reports/
#     │   └── usage_2024-06-01.csv
#     ├── resmon/
#     │   └── version.txt
# 
# Pre-task file contents:
# 
# /home/user/projects/resmon/CHANGELOG.md:
# -----------------------------------------
# ## [1.4.2] - 2024-06-01
# - Improved resource usage reporting accuracy.
# 
# (There is no [Unreleased] section yet—agent must add it.)
# 
# /home/user/projects/resmon/reports/usage_2024-06-01.csv:
# --------------------------------------------------------
# resource,cpu_usage,mem_usage
# web01,45,78
# db01,67,85
# api01,55,72
# 
# /home/user/projects/resmon/resmon/version.txt:
# ----------------------------------------------
# 1.4.2
# 
# EXPECTED POST-TASK STATE:
# 
# /home/user/projects/resmon/resmon/version.txt:
# ----------------------------------------------
# 1.5.0
# 
# /home/user/projects/resmon/CHANGELOG.md:
# ----------------------------------------
# ## [1.5.0] - 2024-06-02
# - Added disk I/O statistics collection to the monitoring tool.
# 
# ## [1.4.2] - 2024-06-01
# - Improved resource usage reporting accuracy.
# 
# /home/user/projects/resmon/reports/release_2024-06-02.log:
# -----------------------------------------------------------
# 1.5.0
# - Added disk I/O statistics collection to the monitoring tool.
# Disk I/O statistics monitoring is now available as part of the resource usage tool.
# 
# /home/user/projects/resmon/reports/usage_2024-06-01.csv:
# (unchanged throughout the task)
# 
# No additional or extra whitespace, comments, or sections should be present. File order, section order, and entry verbatim content as above.

echo 'No automated solution provided.'
