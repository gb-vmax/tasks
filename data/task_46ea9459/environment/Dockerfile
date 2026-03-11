FROM endless-deps-1675428c4810:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/databases

# Create source database
python3 - <<'EOF'
import sqlite3

conn = sqlite3.connect("/home/user/databases/source.db")
conn.execute("""
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    balance REAL NOT NULL,
    created_at TEXT NOT NULL
)
""")
conn.execute("INSERT INTO customers VALUES (1, 'Alice Nguyen', 'alice@example.com', 450.75, '2024-01-10')")
conn.execute("INSERT INTO customers VALUES (2, 'Bob Martinez', 'bob@example.com', 1200.00, '2024-01-12')")
conn.execute("INSERT INTO customers VALUES (3, 'Carol Smith', 'carol@example.com', 89.50, '2024-01-15')")
conn.execute("INSERT INTO customers VALUES (4, 'David Lee', 'david@example.com', 3300.25, '2024-01-18')")
conn.execute("INSERT INTO customers VALUES (5, 'Eva Chen', 'eva@example.com', 760.00, '2024-01-20')")
conn.commit()
conn.close()
EOF

# Create migrated database (missing id=3)
python3 - <<'EOF'
import sqlite3

conn = sqlite3.connect("/home/user/databases/migrated.db")
conn.execute("""
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    balance REAL NOT NULL,
    created_at TEXT NOT NULL
)
""")
conn.execute("INSERT INTO customers VALUES (1, 'Alice Nguyen', 'alice@example.com', 450.75, '2024-01-10')")
conn.execute("INSERT INTO customers VALUES (2, 'Bob Martinez', 'bob@example.com', 1200.00, '2024-01-12')")
conn.execute("INSERT INTO customers VALUES (4, 'David Lee', 'david@example.com', 3300.25, '2024-01-18')")
conn.execute("INSERT INTO customers VALUES (5, 'Eva Chen', 'eva@example.com', 760.00, '2024-01-20')")
conn.commit()
conn.close()
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
