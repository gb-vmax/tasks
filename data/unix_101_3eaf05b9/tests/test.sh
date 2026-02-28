#!/bin/bash
if [ "$(whoami)" = "user" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
