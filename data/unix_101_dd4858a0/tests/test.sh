#!/bin/bash
if [ ! -f /home/user/interfaces.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if ! grep -qE 'Iface|Kernel' /home/user/interfaces.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if [ $(wc -l < /home/user/interfaces.txt) -lt 2 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
echo 1 > /logs/verifier/reward.txt
