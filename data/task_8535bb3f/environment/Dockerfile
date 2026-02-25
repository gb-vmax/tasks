FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install Python3, pip, sqlite3, and pytest
    apt-get update
    apt-get install -y python3 python3-pip sqlite3
    pip3 install --no-cache-dir pytest

    # Create user home directory if not exists
    mkdir -p /home/user

    # Create the sample source sqlite3 database with the required schema and data
    cd /home/user
    sqlite3 source_data.db <<EOF
CREATE TABLE employee (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER
);
INSERT INTO employee (id, name, salary) VALUES (1, 'Alice', 60000);
INSERT INTO employee (id, name, salary) VALUES (2, 'Bob', 70000);
INSERT INTO employee (id, name, salary) VALUES (3, 'Carol', 65000);
EOF

    # Set permissions so non-root users can access the files
    chmod 755 /home/user
    chmod 644 /home/user/source_data.db
ENDPOST

WORKDIR /home/user
