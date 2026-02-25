FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create user and home directory if not already present
    if ! id user >/dev/null 2>&1; then
        useradd -m -s /bin/bash user
    fi

    # Ensure /home/user exists and is owned by user
    mkdir -p /home/user
    chown user:user /home/user

    # Create /home/user/db directory and set permissions
    mkdir -p /home/user/db
    chown user:user /home/user/db
    chmod 700 /home/user/db

    # Create /home/user/db/query.log with specified contents
    cat > /home/user/db/query.log <<'EOF'
[2024-06-20 13:27:14] user:alice db:invoices duration:205ms query:SELECT * FROM payments WHERE amount > 1000;
[2024-06-20 13:28:10] user:bob db:customers duration:98ms query:SELECT * FROM customers WHERE country='US';
[2024-06-20 13:29:45] user:carol db:invoices duration:201ms query:UPDATE invoices SET status='paid' WHERE id=42;
[2024-06-20 13:30:55] user:dave db:payments duration:199ms query:DELETE FROM payments WHERE amount < 10;
[2024-06-20 13:31:16] user:alice db:accounts duration:305ms query:INSERT INTO accounts (user, balance) VALUES ('alice', 500);
EOF
    chown user:user /home/user/db/query.log
    chmod 600 /home/user/db/query.log

    # Ensure slow_queries.log does not exist
    rm -f /home/user/db/slow_queries.log
ENDPOST

WORKDIR /home/user
