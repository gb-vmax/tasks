#!/bin/bash
set -e
cd /home/user

sqlite3 /home/user/source_data.db ".schema employee"
sqlite3 /home/user/destination_data.db "CREATE TABLE employee (id INTEGER PRIMARY KEY, name TEXT, salary INTEGER);"
sqlite3 /home/user/source_data.db ".dump employee" | grep '^INSERT' | sqlite3 /home/user/destination_data.db
cat > /home/user/validate_migration.py << 'EOF'
import sqlite3

src_db = "/home/user/source_data.db"
dst_db = "/home/user/destination_data.db"
report_path = "/home/user/migration_report.txt"

def get_rows(db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT id, name, salary FROM employee ORDER BY id ASC;")
    rows = cur.fetchall()
    conn.close()
    return rows

src_rows = get_rows(src_db)
dst_rows = get_rows(dst_db)

total_row_match = "YES" if len(src_rows) == len(dst_rows) else "NO"
data_integrity = "PASSED" if src_rows == dst_rows else "FAILED"

with open(report_path, "w") as f:
    f.write(f"TOTAL ROWS MATCH: {total_row_match}\n")
    f.write(f"DATA INTEGRITY: {data_integrity}\n")
    for s, d in zip(src_rows, dst_rows):
        f.write(f"source_row={{'id': {s[0]}, 'name': {repr(s[1])}, 'salary': {s[2]}}} ")
        f.write(f"destination_row={{'id': {d[0]}, 'name': {repr(d[1])}, 'salary': {d[2]}}}\n")
EOF
python3 /home/user/validate_migration.py
cat /home/user/migration_report.txt
