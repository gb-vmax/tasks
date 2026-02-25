#!/bin/bash
set -e
cd /home/user

awk '{if ($1 ~ /^[0-9]{1,3}(\.[0-9]{1,3}){3}$/) ips[$1]++} END {for (ip in ips) print ip, ips[ip]}' /home/user/investigation/access.log | awk '{ips[$2][$1]=$0; counts[$2]++} END { n=asorti(counts, carray, "@ind_num_desc"); for (i=1; i<=n; i++) { cnt=carray[i]; split("", iparray); m=0; for (ip in ips[cnt]) { iparray[++m]=ip }; asort(iparray); for(j=1;j<=m;j++) print ips[cnt][iparray[j]] } }' > /home/user/investigation/ip_report.txt
awk '
$1 ~ /^[0-9]{1,3}(\.[0-9]{1,3}){3}$/ { count[$1]++ }
END {
  n = asorti(count, ips)
  for (i = 1; i <= n; i++) result[i] = ips[i]

  # Now selection sort and print by count descending, IP ascending for ties
  while (n > 0) {
    maxidx = 1
    for (i = 2; i <= n; i++) {
      if (count[result[i]] > count[result[maxidx]] ||
         (count[result[i]] == count[result[maxidx]] && result[i] < result[maxidx]))
        maxidx = i
    }
    print result[maxidx], count[result[maxidx]]
    # Remove this entry
    for (i = maxidx; i < n; i++) result[i] = result[i+1]
    n--
  }
}
' /home/user/investigation/access.log > /home/user/investigation/ip_report.txt
awk '
$1 ~ /^[0-9]{1,3}(\.[0-9]{1,3}){3}$/ { 
  if (!( $1 in seen)) { ips[++n] = $1; seen[$1]=1 }
  count[$1]++ 
}
END {
  while (1) {
    max = -1
    delete candidates
    # Find the max count among unprocessed IPs
    for (i = 1; i <= n; i++) {
      ip = ips[i]
      if (count[ip] > max) max = count[ip]
    }
    if (max < 0) break
    # Gather all IPs with this count
    for (i = 1; i <= n; i++) {
      ip = ips[i]
      if (count[ip] == max) candidates[ip]=1
    }
    # Lexicographically sort candidate IPs (selection technique)
    while (length(candidates) > 0) {
      minip = ""
      for (ip in candidates) {
        if (minip == "" || ip < minip) minip = ip
      }
      print minip, max
      count[minip] = -1
      delete candidates[minip]
    }
  }
}
' /home/user/investigation/access.log > /home/user/investigation/ip_report.txt
cat /home/user/investigation/ip_report.txt
head -10 /home/user/investigation/access.log
awk '$1 ~ /^[0-9]{1,3}(\.[0-9]{1,3}){3}$/ { print $1 }' /home/user/investigation/access.log
awk '{print $1}' /home/user/investigation/access.log
awk '$1 ~ /^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$/ { print $1 }' /home/user/investigation/access.log
awk '
$1 ~ /^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$/ { 
  if (!($1 in seen)) { ips[++n] = $1; seen[$1]=1 }
  count[$1]++ 
}
END {
  while (1) {
    max = -1
    delete candidates
    for (i = 1; i <= n; i++) {
      ip = ips[i]
      if (count[ip] > max) max = count[ip]
    }
    if (max < 0) break
    for (i = 1; i <= n; i++) {
      ip = ips[i]
      if (count[ip] == max) candidates[ip]=1
    }
    while (length(candidates) > 0) {
      minip = ""
      for (ip in candidates) {
        if (minip == "" || ip < minip) minip = ip
      }
      print minip, max
      count[minip] = -1
      delete candidates[minip]
    }
  }
}
' /home/user/investigation/access.log > /home/user/investigation/ip_report.txt
cat /home/user/investigation/ip_report.txt
