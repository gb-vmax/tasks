#!/bin/bash
# Ground truth reference (not an executable solution):
#
# # Pre-existing /home/user/workflows/build.yml:
# # (kept simple for this single-command task)
# # Do NOT show this to the agent.
# 
# File: /home/user/workflows/build.yml
# Content before editing:
# steps:
#   - name: checkout
#     run: git checkout .
#   - name: test
#     run: ./test.sh
# 
# Content after correct edit:
# steps:
#   - name: checkout
#     run: git checkout .
#   - name: test
#     run: ./test.sh
#   - name: deploy
#     run: ./deploy.sh
# 
# File: /home/user/workflows/edit.log
# Content:
# Step 'deploy' added to build.yml
# 
# # All files are created with default user permissions and owned by user.
# # Directory /home/user/workflows/ exists and is writable.

echo 'No automated solution provided.'
