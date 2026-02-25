#!/bin/bash
set -e
cd /home/user

wc -l < /home/user/ping_results.log
grep "100% packet loss" /home/user/ping_results.log | sed -n 's/.*Host: \(.*\) Result: 100% packet loss/\1/p'
grep "100% packet loss" /home/user/ping_results.log > /home/user/unreachable_hosts.log
