#!/bin/bash
set -e
cd /home/user

awk '$4 == "MISSING" || $4 == "PARTIAL" {print $2, $3, $4}' /home/user/projects/localization/update_logs/translations_update.log | sort -k1,1 -k2,2 | uniq | awk 'BEGIN{lang=""} {if($1!=lang){if(lang!=""){print ""}lang=$1; print "["lang"]"} print $2": "$3}' > /home/user/projects/localization/update_reports/untranslated_summary.txt && echo "Summary report created at /home/user/projects/localization/update_reports/untranslated_summary.txt"
