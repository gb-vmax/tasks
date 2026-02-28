#!/bin/bash
if [ -s /logs/verifier/stdout.txt ]; then echo 0 > /logs/verifier/reward.txt; else echo 1 > /logs/verifier/reward.txt; fi
