#!/bin/bash
# Ground truth reference (not an executable solution):
#
# Before the task starts, the following files and directories exist:
# - /home/user/storage_audit/
# - /home/user/storage_audit/subdir1/
# - /home/user/storage_audit/subdir2/
# - /home/user/storage_audit/subdir1/largefile1.bin : A file of 15MB. Contents do not include the word "password".
# - /home/user/storage_audit/subdir2/largefile2.txt : A file of 22MB. On line 53, it contains the text: "This file contains the password: hunter2".
# - /home/user/storage_audit/smallfile.txt : A file of 2KB, does not contain the word "password".
# - /home/user/storage_audit/subdir2/largefile3.dat : A file of 11MB, which, on line 1, contains: "PASSWORD = \"secretphrase\"".
# - /home/user/storage_audit/unrelatedfile.log : A file of 500 bytes, does not contain the word "password".
# 
# After the agent completes the task, the following file must exist:
# 
# /home/user/storage_audit/security_scan.log
# 
# Contents of /home/user/storage_audit/security_scan.log (line-endings: LF):
# 
# /home/user/storage_audit/subdir1/largefile1.bin: OK No sensitive keywords found.
# /home/user/storage_audit/subdir2/largefile2.txt: ALERT Keyword 'password' found on line 53
# /home/user/storage_audit/subdir2/largefile3.dat: ALERT Keyword 'password' found on line 1
# 
# Order of lines does not matter, but all must be present and correctly formatted as above.
# 
# No log entry should be present for /home/user/storage_audit/smallfile.txt or /home/user/storage_audit/unrelatedfile.log or any file 10MB or smaller.

echo 'No automated solution provided.'
