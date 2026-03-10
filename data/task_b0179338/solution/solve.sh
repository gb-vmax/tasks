#!/bin/bash
set -e
cd /home/user

cat /home/user/docs/api_endpoints.txt
grep -oP '(?<=/)\S+' /home/user/docs/api_endpoints.txt | sed 's|^|/|' | sort -u > /home/user/docs/endpoints_index.txt && cat /home/user/docs/endpoints_index.txt
grep '^\[GET\]' /home/user/docs/api_endpoints.txt > /home/user/docs/get_endpoints.txt && cat /home/user/docs/get_endpoints.txt
grep -oP '(?<=\[)\w+(?=\])' /home/user/docs/api_endpoints.txt | sort | uniq -c | awk '{print $2": "$1}' | sort > /home/user/docs/endpoints_summary.txt && cat /home/user/docs/endpoints_summary.txt
