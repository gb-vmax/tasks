FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/backups
mkdir -p /tmp/backup_src/data

echo '{"env":"production","version":"3.1.4","debug":false}' > /tmp/backup_src/data/config.json
printf 'id,name,email\n1,Alice,alice@example.com\n2,Bob,bob@example.com\n3,Carol,carol@example.com\n' > /tmp/backup_src/data/users.csv
printf 'Backup taken at 2024-11-01 02:00:00 UTC.\nAll systems nominal.\n' > /tmp/backup_src/data/notes.txt

cd /tmp/backup_src && tar -czf /home/user/backups/nightly.tar.gz data/

# Generate manifest with paths relative to what they'll be after extraction
cd /tmp/backup_src && sha256sum data/config.json data/users.csv data/notes.txt > /home/user/backups/manifest.sha256

rm -rf /tmp/backup_src

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
