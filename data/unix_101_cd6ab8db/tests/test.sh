#!/bin/bash
if [ ! -f /home/user/gamma.c ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
if grep -q '#include <stdio.h>' /home/user/gamma.c && grep -q 'int main()' /home/user/gamma.c; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
