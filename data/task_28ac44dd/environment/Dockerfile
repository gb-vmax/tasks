FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install Python3, pip, and pytest
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install --no-cache-dir pytest

    # Create user, home, and db directories
    useradd -m user
    mkdir -p /home/user/db

    # Set permissions so user can read/write in their home
    chown -R user:user /home/user

    # Create /home/user/db/postgresql.log with the required content
    cat > /home/user/db/postgresql.log <<EOF
[2024-05-22 14:23:11] user=alice db=inventory duration=145ms statement: SELECT * FROM products;
[2024-05-22 14:25:42] user=bob db=sales duration=384ms statement: UPDATE orders SET status='shipped' WHERE id=1492;
[2024-05-22 14:26:00] user=carol db=inventory duration=92ms statement: DELETE FROM products WHERE id=3482;
[2024-05-22 14:27:03] user=dan db=inventory duration=518ms statement: INSERT INTO products VALUES (1023, 'pen', 1.20);
[2024-05-22 14:30:14] user=alice db=sales duration=215ms statement: SELECT * FROM orders WHERE status='shipped';
[2024-05-22 14:31:22] user=dan db=inventory duration=301ms statement: SELECT COUNT(*) FROM products;
[2024-05-22 14:32:45] user=bob db=sales duration=44ms statement: SELECT * FROM customers;
EOF

    # Set permissions so user can access their db directory and files
    chown -R user:user /home/user/db
    chmod 700 /home/user
    chmod 700 /home/user/db
    chmod 600 /home/user/db/postgresql.log
ENDPOST

WORKDIR /home/user
