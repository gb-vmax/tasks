#!/bin/bash
set -e
cd /home/user

tar -czpf /home/user/ml_experiments/exp_42_backup_$(date +%Y%m%d).tar.gz -C /home/user/ml_experiments exp_42
cd /home/user/ml_experiments && sha256sum exp_42_backup_$(date +%Y%m%d).tar.gz | sed 's/  /  /' > exp_42_backup_$(date +%Y%m%d).sha256
archive_date=$(date +%Y%m%d)
backup_date=$(date +%F)
archive_name="exp_42_backup_${archive_date}.tar.gz"
archive_path="/home/user/ml_experiments/$archive_name"
archive_size=$(stat -c%s "$archive_path")
sha256_hash=$(cut -d' ' -f1 /home/user/ml_experiments/exp_42_backup_${archive_date}.sha256)
cat <<EOF > /home/user/ml_experiments/exp_42/backup.log
Backup Date: $backup_date
Archive Name: $archive_name
Archive Size: $archive_size bytes
SHA256: $sha256_hash
Backup Files:
- model/model.h5
- model/params.json
- logs/train.log
- metrics.csv
EOF
cat /home/user/ml_experiments/exp_42/backup.log
