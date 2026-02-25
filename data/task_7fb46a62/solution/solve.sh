#!/bin/bash
set -euo pipefail

# Copy source.db to destination.db
cp /home/user/source.db /home/user/destination.db

# Get row counts
SRC_COUNT=$(sqlite3 /home/user/source.db "SELECT COUNT(*) FROM customers;")
DST_COUNT=$(sqlite3 /home/user/destination.db "SELECT COUNT(*) FROM customers;")

# Write migration validation log
{
    echo "Total rows in source: ${SRC_COUNT}"
    echo "Total rows in destination: ${DST_COUNT}"
    if [ "$SRC_COUNT" -eq "$DST_COUNT" ]; then
        echo "Row count matches"
    else
        echo "Row count mismatch"
    fi

    # Compare row contents
    SRC_DATA=$(sqlite3 /home/user/source.db "SELECT id, name, email FROM customers ORDER BY id;")
    DST_DATA=$(sqlite3 /home/user/destination.db "SELECT id, name, email FROM customers ORDER BY id;")
    if [ "$SRC_DATA" = "$DST_DATA" ]; then
        echo "Row contents match"
    else
        echo "Row contents mismatch"
    fi
} > /home/user/migration_validation.log
