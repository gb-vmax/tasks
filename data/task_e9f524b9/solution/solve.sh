#!/bin/bash
set -e
cd /home/user

ls /home/user/credentials/ && echo "---" && cat /home/user/credentials/db_creds.tsv && echo "---" && cat /home/user/credentials/api_creds.tsv && echo "---" && cat /home/user/credentials/ssh_creds.tsv
cd /home/user/credentials

# Process db_creds: service(5), host(3), username(2), secret=password(1), port(4)
tail -n +2 db_creds.tsv | cut -f5,3,2,1,4 > db_transformed.tsv

# Process api_creds: service(1), host(2), username(3), secret=api_key(4), port=N/A
tail -n +2 api_creds.tsv | cut -f1,2,3,4 | awk 'BEGIN{OFS="\t"}{print $0"\tN/A"}' > api_transformed.tsv

# Process ssh_creds: service(5), host(1), username(2), secret=key_fingerprint(3), port(4)
tail -n +2 ssh_creds.tsv | cut -f5,1,2,3,4 > ssh_transformed.tsv

echo "=== db_transformed ===" && cat db_transformed.tsv
echo "=== api_transformed ===" && cat api_transformed.tsv
echo "=== ssh_transformed ===" && cat ssh_transformed.tsv
cd /home/user/credentials

# Process db_creds: service($5), host($3), username($2), secret=password($1), port($4)
tail -n +2 db_creds.tsv | awk 'BEGIN{OFS="\t"}{print $5,$3,$2,$1,$4}' > db_transformed.tsv

# Process api_creds: service($1), host($2), username($3), secret=api_key($4), port=N/A
tail -n +2 api_creds.tsv | awk 'BEGIN{OFS="\t"}{print $1,$2,$3,$4,"N/A"}' > api_transformed.tsv

# Process ssh_creds: service($5), host($1), username($2), secret=key_fingerprint($3), port($4)
tail -n +2 ssh_creds.tsv | awk 'BEGIN{OFS="\t"}{print $5,$1,$2,$3,$4}' > ssh_transformed.tsv

echo "=== db_transformed ===" && cat db_transformed.tsv
echo "=== api_transformed ===" && cat api_transformed.tsv
echo "=== ssh_transformed ===" && cat ssh_transformed.tsv
cd /home/user/credentials

# Create rotation_report.tsv with header + all three transformed files
{ printf 'service\thost\tusername\tsecret\tport\n'; cat db_transformed.tsv api_transformed.tsv ssh_transformed.tsv; } > rotation_report.tsv

cat rotation_report.tsv
cd /home/user/credentials

# Count rows in each transformed file
db_count=$(wc -l < db_transformed.tsv)
api_count=$(wc -l < api_transformed.tsv)
ssh_count=$(wc -l < ssh_transformed.tsv)
total=$((db_count + api_count + ssh_count))

# Get sorted unique services from the report (skip header, col1)
services=$(tail -n +2 rotation_report.tsv | cut -f1 | sort -u | tr '\n' ',' | sed 's/,/, /g; s/, $//')

cat > rotation_summary.txt <<EOF
Total credentials: $total
DB credentials: $db_count
API credentials: $api_count
SSH credentials: $ssh_count
Services: $services
EOF

cat rotation_summary.txt
cd /home/user/credentials

echo "=== rotation_report.tsv ===" && cat rotation_report.tsv
echo ""
echo "=== rotation_summary.txt ===" && cat rotation_summary.txt
echo ""
echo "=== Cleanup temp files ===" && rm db_transformed.tsv api_transformed.tsv ssh_transformed.tsv && ls
