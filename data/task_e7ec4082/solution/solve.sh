#!/bin/bash
set -e
cd /home/user

head -20 /home/user/logs/access.log
wc -l /home/user/logs/access.log && tail -20 /home/user/logs/access.log
mkdir -p /home/user/reports && cat /home/user/logs/access.log | awk '
{
    ip = $1
    method = substr($6, 2)
    status = $9
    bytes_field = $10

    ip_count[ip]++
    status_count[status]++

    bytes_val = (bytes_field == "-") ? 0 : bytes_field + 0
    method_bytes[method] += bytes_val

    if (status + 0 >= 400) {
        ip_errors[ip]++
    }
}
END {
    for (ip in ip_count) {
        print ip_count[ip] "\t" ip > "/tmp/ip_counts.txt"
    }
    for (s in status_count) {
        print s "\t" status_count[s] > "/tmp/status_counts.txt"
    }
    for (m in method_bytes) {
        print m "\t" method_bytes[m] > "/tmp/method_bytes.txt"
    }
    for (ip in ip_count) {
        errs = (ip in ip_errors) ? ip_errors[ip] : 0
        total = ip_count[ip]
        if (total >= 3 && errs * 2 > total) {
            print ip "\t" errs "\t" total > "/tmp/suspicious.txt"
        }
    }
}
'
cat /tmp/ip_counts.txt && echo "---" && cat /tmp/status_counts.txt && echo "---" && cat /tmp/method_bytes.txt && echo "---" && cat /tmp/suspicious.txt 2>/dev/null || echo "none"
# Sort top 5 IPs: count desc, then IP asc
sort -t$'\t' -k1,1rn -k2,2 /tmp/ip_counts.txt | head -5 > /tmp/top5_ips.txt
cat /tmp/top5_ips.txt
sort -t$'\t' -k1,1n /tmp/status_counts.txt > /tmp/status_sorted.txt && cat /tmp/status_sorted.txt
sort -t$'\t' -k1,1 /tmp/method_bytes.txt > /tmp/method_sorted.txt && cat /tmp/method_sorted.txt
sort -t$'\t' -k2,2rn -k1,1 /tmp/suspicious.txt > /tmp/suspicious_sorted.txt && cat /tmp/suspicious_sorted.txt 2>/dev/null || echo "empty"
{
  echo "=== TRAFFIC REPORT ==="
  echo ""
  echo "--- Top 5 IPs by Request Count ---"
  awk '{print $1 "\t" $2}' /tmp/top5_ips.txt
  echo ""
  echo "--- Status Code Summary ---"
  awk '{print $1 ": " $2 " requests"}' /tmp/status_sorted.txt
  echo ""
  echo "--- Total Bytes Transferred by Method ---"
  awk '{print $1 ": " $2 " bytes"}' /tmp/method_sorted.txt
  echo ""
  echo "--- Suspicious IPs (error rate > 50%) ---"
  if [ -s /tmp/suspicious_sorted.txt ]; then
    awk '{print $1 " errors=" $2 " total=" $3}' /tmp/suspicious_sorted.txt
  else
    echo "None"
  fi
} > /home/user/reports/traffic_report.txt
cat /home/user/reports/traffic_report.txt
xxd /home/user/reports/traffic_report.txt | tail -3
od -c /home/user/reports/traffic_report.txt | tail -3
cat -A /home/user/reports/traffic_report.txt | head -10
