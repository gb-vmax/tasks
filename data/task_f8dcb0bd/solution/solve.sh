#!/bin/bash
set -euo pipefail

# Count ticket frequencies, sort by count descending, then title ascending for ties
sort /home/user/ticket_titles.txt | uniq -c | sort -k1,1rn -k2 | sed 's/^ *//' > /home/user/ticket_frequency_report.txt
