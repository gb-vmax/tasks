FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create backup directories
mkdir -p /home/user/backups/pg

# Write all four backup files with their VALID contents first
printf 'PGDUMP_PRIMARY_20240801_DATA_BLOCK_VALID' > /home/user/backups/pg/db_primary_20240801.dump
printf 'PGDUMP_REPLICA_20240801_DATA_BLOCK_VALID' > /home/user/backups/pg/db_replica_20240801.dump
printf 'PGDUMP_PRIMARY_20240731_DATA_BLOCK_VALID' > /home/user/backups/pg/db_primary_20240731.dump
printf 'PGDUMP_REPLICA_20240731_DATA_BLOCK_VALID' > /home/user/backups/pg/db_replica_20240731.dump

# Generate checksums manifest with full paths, in the required order
sha256sum \
    /home/user/backups/pg/db_primary_20240801.dump \
    /home/user/backups/pg/db_replica_20240801.dump \
    /home/user/backups/pg/db_primary_20240731.dump \
    /home/user/backups/pg/db_replica_20240731.dump \
    > /home/user/backups/pg/checksums.sha256

# Now corrupt db_primary_20240731.dump AFTER generating the checksums
# so its hash no longer matches the manifest
printf 'PGDUMP_PRIMARY_20240731_DATA_BLOCK_CORRUPTED' > /home/user/backups/pg/db_primary_20240731.dump

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
