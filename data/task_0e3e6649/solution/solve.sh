#!/bin/bash
# Ground truth reference (not an executable solution):
#
# Before the task begins, the following file exists:
# File: /home/user/app_profile.csv
# Contents (with UNIX line endings):
# ProcessID,Process,User,Threads,CPU%,MemoryMB
# 1023,chrome,alice,14,32.5,450
# 1057,firefox,bob,8,42.1,305
# 1092,code,carol,10,15.7,210
# 1107,slack,dan,6,21.0,190
# 
# After task completion, the following file must exist:
# File: /home/user/profile_summary.csv
# Contents (with UNIX line endings):
# Process,CPU%
# chrome,32.5
# firefox,42.1
# code,15.7
# slack,21.0

echo 'No automated solution provided.'
