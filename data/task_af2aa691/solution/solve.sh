#!/bin/bash
set -e
cd /home/user

python3 /home/user/legacy_tool_a/tool_a.py > /home/user/legacy_tool_a/run_output.log & python3 /home/user/legacy_tool_b/tool_b.py > /home/user/legacy_tool_b/run_output.log & wait
mkdir -p /home/user/legacy_scripts_outputs
echo "=== tool_a.py Output ===" > /home/user/legacy_scripts_outputs/summary.log && cat /home/user/legacy_tool_a/run_output.log >> /home/user/legacy_scripts_outputs/summary.log && echo "=== tool_b.py Output ===" >> /home/user/legacy_scripts_outputs/summary.log && cat /home/user/legacy_tool_b/run_output.log >> /home/user/legacy_scripts_outputs/summary.log && echo "[LOG FILES CONFIRMED]
legacy_tool_a/run_output.log
legacy_tool_b/run_output.log
summary.log" >> /home/user/legacy_scripts_outputs/summary.log
cat /home/user/legacy_scripts_outputs/summary.log
