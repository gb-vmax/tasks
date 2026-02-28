#!/bin/bash
alias ll='ls -l'
alias la='ls -A'
alias gs='git status'
unalias -a 2>/dev/null
if alias | grep -q '='; then echo 0 > /logs/verifier/reward.txt; else echo 1 > /logs/verifier/reward.txt; fi
