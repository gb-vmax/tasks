#!/bin/bash
set -e
cd /home/user

awk '/^\[network\]/{p=1; next} /^\[.*\]/{p=0} p && /^[^;#[:space:]]+\s*=/{gsub(/^[[:space:]]+|[[:space:]]+$/, ""); print; c++} END{if(c) print "Total network parameters: " c; else print "Total network parameters: 0"}' /home/user/appconfig/settings.ini > /home/user/appconfig/network_diagnostics.log
cat /home/user/appconfig/network_diagnostics.log
cat /home/user/appconfig/settings.ini
awk 'BEGIN{p=0;c=0} /^\[network\]/{p=1; next} /^\[.*\]/{p=0} p && /^[^;#[:space:]]+\s*=/{gsub(/^[[:space:]]+|[[:space:]]+$/, ""); a[c++]=$0} END{for(i=0;i<c;i++) print a[i]; print "Total network parameters: " c}' /home/user/appconfig/settings.ini > /home/user/appconfig/network_diagnostics.log
cat /home/user/appconfig/network_diagnostics.log
awk 'p && /^[^;#[:space:]]+\s*=/{gsub(/^[[:space:]]+|[[:space:]]+$/, ""); a[c++]=$0} /^\[network\]/{p=1; next} /^\[[^]]+\]/{if(!/\[network\]/)p=0} END{for(i=0;i<c;i++)print a[i]; print "Total network parameters: " c}' /home/user/appconfig/settings.ini > /home/user/appconfig/network_diagnostics.log
cat /home/user/appconfig/network_diagnostics.log
awk '/^\[/{p=($0=="[network]")} p && /^[^;#[:space:]]+\s*=/{print; c++} END{print "Total network parameters: " c+0}' /home/user/appconfig/settings.ini > /home/user/appconfig/network_diagnostics.log
cat /home/user/appconfig/network_diagnostics.log
awk '/^\[network\]/{p=1; next} /^\[/{p=0} p && /^[^;#[:space:]]+\s*=[^=]*/{print; c++} END{print "Total network parameters: " c+0}' /home/user/appconfig/settings.ini > /home/user/appconfig/network_diagnostics.log
cat /home/user/appconfig/network_diagnostics.log
nl -ba /home/user/appconfig/settings.ini
awk '/^\[network\]/{p=1; next} /^\[.*\]/{if ($0 != "[network]") p=0} p && /^[^;#[:space:]]+\s*=\s*.*$/{gsub(/^[[:space:]]+|[[:space:]]+$/, ""); print; c++} END{print "Total network parameters: " c+0}' /home/user/appconfig/settings.ini > /home/user/appconfig/network_diagnostics.log
cat /home/user/appconfig/network_diagnostics.log
awk '/^\[network\]/{p=1; next} /^\[.*\]/{p=0} p && /=/ {print}' /home/user/appconfig/settings.ini
awk '/^\[network\]/{p=1; next} /^\[.*\]/{p=0} p && /=/ {gsub(/^[[:space:]]+|[[:space:]]+$/, "", $0); a[++c]=$0} END{for(i=1;i<=c;i++) print a[i]; print "Total network parameters: " c+0}' /home/user/appconfig/settings.ini > /home/user/appconfig/network_diagnostics.log
