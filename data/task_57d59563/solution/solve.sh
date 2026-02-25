#!/bin/bash
set -e
cd /home/user

mkdir -p hardened_configs

for f in source_configs/*.conf; do
    base=$(basename "$f")
    cp "$f" "hardened_configs/$base"
    printf '%s\n' '# Hardened' >> "hardened_configs/$base"
done
