#!/bin/bash
if [ -f /home/user/output_dir/source/main.py ] && [ -f /home/user/output_dir/source/config/settings.yaml ]; then
  if grep -qxF 'main.py content' /home/user/output_dir/source/main.py && grep -qxF 'config.yaml' /home/user/output_dir/source/config/settings.yaml; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
