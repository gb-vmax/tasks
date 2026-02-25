#!/bin/bash
set -euo pipefail

# Replace alice's API key in api_credentials.csv
sed -i 's/alice,OLD_KEY_12345/alice,NEW_SECURE_API_KEY_8901/' /home/user/security/api_credentials.csv

# Create rotation log (exactly one line with trailing newline)
printf "alice's API key rotated to NEW_SECURE_API_KEY_8901\n" > /home/user/security/rotation_log.txt
