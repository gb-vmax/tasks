FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install required packages: python3, pip, sqlite3
    apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        python3 \
        python3-pip \
        sqlite3

    # Install pytest
    pip3 install pytest

    # Create the migration directory and set permissions
    mkdir -p /home/user/db-migration
    chown -R 1000:1000 /home/user/db-migration
    chmod 755 /home/user
    chmod 777 /home/user/db-migration

    # Create source.db with the required schema and data
    cd /home/user/db-migration

    # Remove any pre-existing db files (defensive)
    rm -f source.db target.db

    # Create source.db and insert 3 records
    sqlite3 source.db <<EOF
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, email TEXT);
INSERT INTO customers (id, name, email) VALUES (1, 'Alice Smith', 'alice.smith@example.com');
INSERT INTO customers (id, name, email) VALUES (2, 'Bob Johnson', 'bob.johnson@example.com');
INSERT INTO customers (id, name, email) VALUES (3, 'Carol Williams', 'carol.williams@example.com');
EOF

    # Create target.db with the same schema, but leave it empty
    sqlite3 target.db <<EOF
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, email TEXT);
EOF

    # Ensure ownership and permissions for agent (user:group 1000:1000, mode 666 for files)
    chown 1000:1000 source.db target.db
    chmod 666 source.db target.db
ENDPOST

WORKDIR /home/user
