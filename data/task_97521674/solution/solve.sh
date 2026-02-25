#!/bin/bash
set -e
cd /home/user

egrep 'locale:(fr|de) \|.*status:(failed|updated) ' /home/user/projects/translation_logs/update_20240612.log > /home/user/projects/translation_logs/filtered_update_20240612.log
N=$(wc -l < /home/user/projects/translation_logs/filtered_update_20240612.log); echo "$N"; echo "SUMMARY: $N entries matching (locale: fr|de, status: failed|updated)" >> /home/user/projects/translation_logs/filtered_update_20240612.log
cat /home/user/projects/translation_logs/filtered_update_20240612.log
