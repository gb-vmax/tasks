#!/bin/bash
PASS=1
arp -n -i dummy1 | grep '10.10.10.2' | grep -i '00:aa:bb:cc:dd:ee' >/dev/null || PASS=0
arp -n -i dummy1 | grep '10.10.10.3' | grep -i '00:11:22:33:44:66' >/dev/null || PASS=0
echo $PASS > /logs/verifier/reward.txt
