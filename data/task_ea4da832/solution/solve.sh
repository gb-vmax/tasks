#!/bin/bash
set -euo pipefail

LOC_DIR="/home/user/localization"
SOURCE="${LOC_DIR}/source.txt"
OLD_FR="${LOC_DIR}/old_fr.txt"
NEW_FR="${LOC_DIR}/new_fr.txt"
UPDATE_LOG="${LOC_DIR}/update.log"

# Clear output files
> "$NEW_FR"
> "$UPDATE_LOG"

# Read old_fr.txt into an associative array (key=phrase, value=translation)
declare -A translations
while IFS='=' read -r key value; do
    translations["$key"]="$value"
done < "$OLD_FR"

# Process each phrase in source.txt
while IFS= read -r phrase; do
    if [ -n "${translations[$phrase]+x}" ]; then
        # Translation exists
        echo "${phrase}=${translations[$phrase]}" >> "$NEW_FR"
        echo "COPIED: ${phrase}" >> "$UPDATE_LOG"
    else
        # Translation missing
        echo "${phrase}=" >> "$NEW_FR"
        echo "MISSING: ${phrase}" >> "$UPDATE_LOG"
    fi
done < "$SOURCE"
