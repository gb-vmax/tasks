#!/bin/bash
set -euo pipefail

# Read CSV lines and filter approved deployments (field 5 = "yes")
# Format: RELEASE <id>: <name> v<version> scheduled for <date>
while IFS=',' read -r id name version date approved; do
    if [ "$approved" = "yes" ]; then
        echo "RELEASE ${id}: ${name} v${version} scheduled for ${date}"
    fi
done < /home/user/releases/pending_deployments.csv > /home/user/releases/deployments_ready.txt
