#!/bin/bash
set -e
cd /home/user

chmod -R go-w /home/user/mlops_artifacts/
{
g_w=$(stat -c %A /home/user/mlops_artifacts/ | cut -c6);
o_w=$(stat -c %A /home/user/mlops_artifacts/ | cut -c9);
[[ $g_w == "w" ]] && g_ans="yes" || g_ans="no";
[[ $o_w == "w" ]] && o_ans="yes" || o_ans="no";
find /home/user/mlops_artifacts/ -perm -g=w -o -perm -o=w | grep -q . && a_ans="no" || a_ans="yes";
printf "Directory: /home/user/mlops_artifacts/\nWritable by group: %s\nWritable by others: %s\nAll files and subdirectories now writable only by owner: %s\n" "$g_ans" "$o_ans" "$a_ans" > /home/user/artifact_permission_fix.log;
}
cat /home/user/artifact_permission_fix.log
