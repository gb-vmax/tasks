#!/bin/bash
set -e
cd /home/user

head -5 /home/user/audit/access_log.tsv
{ echo -e "username\tserver_id\taccess_level\ttimestamp"; awk 'NR>1 {print $2"\t"$3"\t"$5"\t"$1}' FS='\t' /home/user/audit/access_log.tsv; } > /home/user/audit/compliance_report.tsv
cat /home/user/audit/compliance_report.tsv
