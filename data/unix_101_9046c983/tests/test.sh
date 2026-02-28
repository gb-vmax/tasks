#!/bin/bash
export PROJECT=alpha
bash -c 'if [[ "$PROJECT" == "alpha" ]]; then exit 0; else exit 1; fi'
if bash -c 'echo $PROJECT' | grep -q '^alpha$'; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
