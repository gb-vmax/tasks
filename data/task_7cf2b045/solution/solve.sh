#!/bin/bash
# Ground truth reference (not an executable solution):
#
# Before the task begins, the file /home/user/security/api_credentials.csv exists with the following exact content:
# username,apikey
# alice,OLD_KEY_12345
# bob,BOB_API_KEY_555
# carol,CAROL_KEY_6789
# 
# After successful completion, /home/user/security/api_credentials.csv will be:
# username,apikey
# alice,NEW_SECURE_API_KEY_8901
# bob,BOB_API_KEY_555
# carol,CAROL_KEY_6789
# 
# The file /home/user/security/rotation_log.txt will be created with the single exact line:
# alice's API key rotated to NEW_SECURE_API_KEY_8901
# 
# Permissions remain unchanged; user has write access to /home/user/security and its contents.

echo 'No automated solution provided.'
