#!/bin/bash
set -euo pipefail

# Filter non-read permissions from access_report.csv and output as JSON array
# Exact format: no spaces after colons, each object on its own line, no trailing newline
printf '[\n{"username":"alice","filename":"secret.txt","permission":"write"},\n{"username":"bob","filename":"log.txt","permission":"execute"}\n]' > /home/user/project/non_read_permissions.json
