#!/bin/bash
alias gs='git status'
alias ll='ls -l'
alias la='ls -a'
unalias -a
if alias | grep -q '='; then echo 0 > /logs/verifier/reward.txt; else echo 1 > /logs/verifier/reward.txt; fi
