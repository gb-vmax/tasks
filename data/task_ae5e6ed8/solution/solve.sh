#!/bin/bash
set -e
cd /home/user

bash -c '
log="/home/user/logs/access.log"
out="/home/user/logs/analysis_report.txt"
total=$(wc -l &lt; "$log")
notfound=$(awk '\''$9 == 404{c++} END{print c+0}'\'' "$log")
ips=$(awk '\''{print $1}'\'' "$log" | sort -u | paste -sd, -)
read peak hour &lt; &lt;(awk -F[\[:'] '\''{h=sprintf("%02d",$2+0); a[h]++} END{for(i in a) if(a[i]&gt;max){max=a[i]; hh=i} print max,hh}'\'' &lt;(awk '\''{match($0,/\[([0-9]{2})/,a); print a[1]}'\'' "$log"))
echo "Total Requests: $total
404 Errors: $notfound
Unique IPs: $ips
Peak Hour: $hour ($peak requests)" &gt; "$out"
'
awk '
{ips[$1]=1; hours[substr($4,14,2)]++; total++}
$9=="404"{nf++}
END{
  # Unique IPs formatting
  for(ip in ips) list[++c]=ip;
  n = asorti(list, sorted)
  for(i=1;i<=n;i++) {
    if(i>1) printf "," >> out;
    printf "%s", list[i] >> out;
  }
  # Find peak hour
  max=0; for(h in hours) if(hours[h]>max){max=hours[h]; hh=h}
  close(out)
  # Output report
  print "Total Requests: " total > out
  print "404 Errors: " (nf+0) >> out
  printf "Unique IPs: " >> out
  for(i=1;i<=n;i++) {
    if(i>1) printf "," >> out;
    printf "%s", list[i] >> out;
  }
  print "" >> out
  printf "Peak Hour: %02d (%d requests)\n", hh, max >> out
}' out="/home/user/logs/analysis_report.txt" /home/user/logs/access.log
total=$(wc -l < /home/user/logs/access.log) && \
notfound=$(awk '$9==404{c++}END{print c+0}' /home/user/logs/access.log) && \
unique_ips=$(awk '{print $1}' /home/user/logs/access.log | sort | uniq | paste -sd, -) && \
read peak_count peak_hour <<< "$(awk '{match($0,/\[([0-9]{2}):/,a); if(a[1]!="") h[a[1]]++} END{for (k in h) print h[k],k}' /home/user/logs/access.log | sort -k1,1nr -k2 | head -n1)" && \
printf "Total Requests: %s\n404 Errors: %s\nUnique IPs: %s\nPeak Hour: %02d (%s requests)\n" "$total" "$notfound" "$unique_ips" "$peak_hour" "$peak_count" > /home/user/logs/analysis_report.txt
cat /home/user/logs/analysis_report.txt
total=$(wc -l < /home/user/logs/access.log) && \
notfound=$(awk '$9==404{c++}END{print c+0}' /home/user/logs/access.log) && \
unique_ips=$(awk '{print $1}' /home/user/logs/access.log | sort | uniq | paste -sd, -) && \
read peak_count peak_hour <<< "$(awk '{if(match($0,/\[[^:]+:([0-9]{2}):[0-9]{2}:[0-9]{2}/,a)) h[a[1]]++} END{for (k in h) print h[k],k}' /home/user/logs/access.log | sort -k1,1nr -k2 | head -n1)" && \
printf "Total Requests: %s\n404 Errors: %s\nUnique IPs: %s\nPeak Hour: %02d (%s requests)\n" "$total" "$notfound" "$unique_ips" "$peak_hour" "$peak_count" > /home/user/logs/analysis_report.txt
cat /home/user/logs/analysis_report.txt
total=$(wc -l < /home/user/logs/access.log) && \
notfound=$(awk '$9==404{c++}END{print c+0}' /home/user/logs/access.log) && \
unique_ips=$(awk '{print $1}' /home/user/logs/access.log | sort | uniq | paste -sd, -) && \
read peak_count peak_hour <<< "$(awk '{if(match($0,/\[[^:]+:([0-9]{2}):/,a)) h[a[1]]++} END{for (k in h) print h[k],k}' /home/user/logs/access.log | sort -k1,1nr -k2 | head -n1)" && \
peak_count=${peak_count:-0} && peak_hour=${peak_hour:-00} && \
printf "Total Requests: %s\n404 Errors: %s\nUnique IPs: %s\nPeak Hour: %02d (%s requests)\n" "$total" "$notfound" "$unique_ips" "$peak_hour" "$peak_count" > /home/user/logs/analysis_report.txt
total=$(wc -l < /home/user/logs/access.log) && \
notfound=$(awk '$9==404{c++}END{print c+0}' /home/user/logs/access.log) && \
unique_ips=$(awk '{print $1}' /home/user/logs/access.log | sort | uniq | paste -sd, -) && \
read peak_count peak_hour <<< "$(cut -d[ -f2 /home/user/logs/access.log | cut -d: -f2 | sort | uniq -c | sort -nr | head -1 | awk '{print $1, $2}')" && \
peak_count=${peak_count:-0} && peak_hour=${peak_hour:-00} && \
printf "Total Requests: %s\n404 Errors: %s\nUnique IPs: %s\nPeak Hour: %02d (%s requests)\n" "$total" "$notfound" "$unique_ips" "$peak_hour" "$peak_count" > /home/user/logs/analysis_report.txt
cat /home/user/logs/analysis_report.txt
