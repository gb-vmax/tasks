FROM endless-base:latest

ENV PATH=/usr/local/bin:/usr/bin:/bin:$PATH

RUN <<'ENDPOST'
apt-get update
    apt-get install -y python3 python3-pip sqlite3
    pip3 install pytest

    # Create the user and home directory if not already present
    useradd -m user || true
    mkdir -p /home/user
    chown user:user /home/user

    # Create the SQLite source database with the required table and rows
    su - user -c "sqlite3 /home/user/source.db <<EOF
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL);
INSERT INTO customers (id, name, email) VALUES (1, 'Alice Smith', 'alice@example.com');
INSERT INTO customers (id, name, email) VALUES (2, 'Bob Jones', 'bob@example.com');
INSERT INTO customers (id, name, email) VALUES (3, 'Carol White', 'carol@example.com');
EOF
"

    # Set permissions so user can read/write their home directory and source.db
    chown user:user /home/user/source.db
    chmod 644 /home/user/source.db
ENDPOST

WORKDIR /home/user
