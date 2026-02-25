#!/bin/bash
set -euo pipefail

LOC_DIR="/home/user/localization"

# Extract French translations from translations.csv (key,fr columns)
# translations.csv has: key,en,fr
{
    echo "key,fr"
    while IFS=',' read -r key en fr; do
        echo "${key},${fr}"
    done < <(tail -n +2 "${LOC_DIR}/translations.csv")
} > "${LOC_DIR}/fr_translations.csv"

# Read fr_updates.csv into associative array
declare -A updates
while IFS=',' read -r key fr; do
    [ "$key" = "key" ] && continue  # skip header
    updates["$key"]="$fr"
done < "${LOC_DIR}/fr_updates.csv"

# Apply updates to create fr_translations_updated.csv and update_log.txt
> "${LOC_DIR}/update_log.txt"
{
    echo "key,fr"
    while IFS=',' read -r key fr; do
        if [ -n "${updates[$key]+x}" ]; then
            new_fr="${updates[$key]}"
            echo "key: ${key} | old_fr: ${fr} | new_fr: ${new_fr}" >> "${LOC_DIR}/update_log.txt"
            echo "${key},${new_fr}"
        else
            echo "${key},${fr}"
        fi
    done < <(tail -n +2 "${LOC_DIR}/fr_translations.csv")
} > "${LOC_DIR}/fr_translations_updated.csv"
