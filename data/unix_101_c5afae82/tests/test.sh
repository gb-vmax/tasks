#!/bin/bash
if grep -qiE '^example.com mail is handled by' /home/user/example_mx.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
