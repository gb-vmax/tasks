#!/bin/bash
set -euo pipefail

# Create logs directory (should already exist from Dockerfile)
mkdir -p /home/user/devops/logs

# List all installed packages sorted alphabetically
dpkg-query -W -f='${Package}\n' | sort > /home/user/devops/logs/installed_packages.txt

# Check for broken packages
BROKEN=$(dpkg --audit 2>&1 || true)

if [ -z "$BROKEN" ]; then
    echo "No broken packages found." > /home/user/devops/logs/package_issues.log
else
    # Parse broken package names from dpkg --audit output
    > /home/user/devops/logs/package_issues.log
    echo "$BROKEN" | while IFS= read -r line; do
        line=$(echo "$line" | xargs)
        [ -z "$line" ] && continue
        if echo "$line" | grep -q ':'; then
            pkg=$(echo "$line" | cut -d: -f1 | xargs)
            if [ -n "$pkg" ] && ! echo "$pkg" | grep -qE '[ \t]'; then
                echo "[BROKEN] $pkg" >> /home/user/devops/logs/package_issues.log
            fi
        fi
    done
    # If no broken packages were actually found in parsing
    if [ ! -s /home/user/devops/logs/package_issues.log ]; then
        echo "No broken packages found." > /home/user/devops/logs/package_issues.log
    fi
fi
