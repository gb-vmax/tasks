#!/bin/bash
alias ll='ls -l'
alias la='ls -A'
alias gs='git status'
unalias ll 2>/dev/null
if alias ll 2>/dev/null; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if alias la 2>/dev/null && alias gs 2>/dev/null; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
