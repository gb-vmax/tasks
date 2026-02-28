#!/bin/bash
if grep -qE '^localhost has address 127\.0\.0\.1' /home/user/host_localhost.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
