#!/bin/bash
set -e
cd /home/user

yml_val=$(grep -m1 '^integrity_check_dir:' /home/user/configs/backup.yml | awk -F ': *' '{print $2}'); toml_val=$(awk '/^\[checks\]/ {f=1; next} /^\[/ {f=0} f && /^\s*integrity_check_dir\s*=/ {sub(/^.*=/,""); gsub(/^[ "\t]+|[ "\t]+$/,""); print; exit}' /home/user/configs/backup.toml); printf "[backup.yml]\nintegrity_check_dir: %s\n\n[backup.toml]\nintegrity_check_dir: %s\n" "$yml_val" "$toml_val" > /home/user/backup_integrity_locations.log
cat /home/user/backup_integrity_locations.log
awk '/^\[checks\]/ {f=1; next} /^\[/ {f=0} f && /integrity_check_dir/ {print}' /home/user/configs/backup.toml
yml_val=$(grep -m1 '^integrity_check_dir:' /home/user/configs/backup.yml | awk -F ': *' '{print $2}'); toml_val=$(awk '/^\[checks\]/ {f=1; next} /^\[/ {f=0} f && /^\s*integrity_check_dir\s*=/ {match($0,/=\s*"?([^"]*)"?/,a); print a[1]; exit}' /home/user/configs/backup.toml); printf "[backup.yml]\nintegrity_check_dir: %s\n\n[backup.toml]\nintegrity_check_dir: %s\n" "$yml_val" "$toml_val" > /home/user/backup_integrity_locations.log
yml_val=$(grep -m1 '^integrity_check_dir:' /home/user/configs/backup.yml | awk -F ': *' '{print $2}'); toml_val=$(awk '/^\[checks\]/ {f=1; next} /^\[/ {f=0} f && /^\s*integrity_check_dir\s*=/ {print $0; exit}' /home/user/configs/backup.toml | sed -e 's/^[^=]*=[[:space:]]*//' -e 's/"//g'); printf "[backup.yml]\nintegrity_check_dir: %s\n\n[backup.toml]\nintegrity_check_dir: %s\n" "$yml_val" "$toml_val" > /home/user/backup_integrity_locations.log
cat /home/user/backup_integrity_locations.log
yml_val=$(grep -m1 '^integrity_check_dir:' /home/user/configs/backup.yml | awk -F ': *' '{print $2}'); toml_val=$(grep -m1 '^\s*integrity_check_dir\s*=' /home/user/configs/backup.toml | sed -e 's/^[^=]*=[[:space:]]*//' -e 's/"//g'); printf "[backup.yml]\nintegrity_check_dir: %s\n\n[backup.toml]\nintegrity_check_dir: %s\n" "$yml_val" "$toml_val" > /home/user/backup_integrity_locations.log
cat /home/user/backup_integrity_locations.log
