#!/bin/bash
alias ll='ls -l'
alias la='ls -a'
unalias ll
if alias ll 2>/dev/null; then echo 0 > /logs/verifier/reward.txt; else echo 1 > /logs/verifier/reward.txt; fi
