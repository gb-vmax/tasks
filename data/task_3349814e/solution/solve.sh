#!/bin/bash
set -e
cd /home/user

cat /home/user/translations/export.tsv
awk 'BEGIN{FS="\t"; OFS="\t"} {gsub(/[[:space:]]+$/, ""); print $1, $4, $3}' /home/user/translations/export.tsv | sed 's/\r//' > /home/user/translations/import_fr.tsv
cat -A /home/user/translations/import_fr.tsv
