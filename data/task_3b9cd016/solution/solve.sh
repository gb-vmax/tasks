#!/bin/bash
set -e
cd /home/user

cat /home/user/tickets/open_tickets.tsv
awk 'BEGIN{FS="\t"; OFS="\t"} {print $1, $7, $3, $5, $2}' /home/user/tickets/open_tickets.tsv > /home/user/tickets/import_ready.tsv
cat /home/user/tickets/import_ready.tsv
