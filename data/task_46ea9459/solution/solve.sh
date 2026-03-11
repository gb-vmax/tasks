#!/bin/bash
set -e
cd /home/user

ls /home/user/databases/
sqlite3 /home/user/databases/source.db "SELECT COUNT(*) FROM customers;"
python3 -c "import sqlite3; conn = sqlite3.connect('/home/user/databases/source.db'); cur = conn.cursor(); cur.execute('SELECT COUNT(*) FROM customers'); print(cur.fetchone())"
python3 << 'EOF'
import sqlite3

src_conn = sqlite3.connect('/home/user/databases/source.db')
mig_conn = sqlite3.connect('/home/user/databases/migrated.db')

src = src_conn.cursor()
mig = mig_conn.cursor()

# Check 1: Row count
src.execute("SELECT COUNT(*) FROM customers")
src_count = src.fetchone()[0]
mig.execute("SELECT COUNT(*) FROM customers")
mig_count = mig.fetchone()[0]
check1_pass = src_count == mig_count

# Check 2: Balance sum
src.execute("SELECT ROUND(SUM(balance), 2) FROM customers")
src_balance = src.fetchone()[0]
mig.execute("SELECT ROUND(SUM(balance), 2) FROM customers")
mig_balance = mig.fetchone()[0]
check2_pass = src_balance == mig_balance

# Check 3: Email uniqueness
src.execute("SELECT COUNT(DISTINCT email) FROM customers")
src_emails = src.fetchone()[0]
mig.execute("SELECT COUNT(DISTINCT email) FROM customers")
mig_emails = mig.fetchone()[0]
check3_pass = src_emails == mig_emails

# Check 4: Missing records
src.execute("SELECT id FROM customers ORDER BY id")
src_ids = set(row[0] for row in src.fetchall())
mig.execute("SELECT id FROM customers ORDER BY id")
mig_ids = set(row[0] for row in mig.fetchall())
missing_ids = sorted(src_ids - mig_ids)
check4_pass = len(missing_ids) == 0

overall_pass = check1_pass and check2_pass and check3_pass and check4_pass

print(f"src_count={src_count}, mig_count={mig_count}")
print(f"src_balance={src_balance}, mig_balance={mig_balance}")
print(f"src_emails={src_emails}, mig_emails={mig_emails}")
print(f"missing_ids={missing_ids}")
print(f"overall={overall_pass}")
EOF
python3 << 'EOF'
import sqlite3

src_conn = sqlite3.connect('/home/user/databases/source.db')
mig_conn = sqlite3.connect('/home/user/databases/migrated.db')

src = src_conn.cursor()
mig = mig_conn.cursor()

# Check 1: Row count
src.execute("SELECT COUNT(*) FROM customers")
src_count = src.fetchone()[0]
mig.execute("SELECT COUNT(*) FROM customers")
mig_count = mig.fetchone()[0]
check1_pass = src_count == mig_count

# Check 2: Balance sum
src.execute("SELECT ROUND(SUM(balance), 2) FROM customers")
src_balance = src.fetchone()[0]
mig.execute("SELECT ROUND(SUM(balance), 2) FROM customers")
mig_balance = mig.fetchone()[0]
check2_pass = src_balance == mig_balance

# Check 3: Email uniqueness
src.execute("SELECT COUNT(DISTINCT email) FROM customers")
src_emails = src.fetchone()[0]
mig.execute("SELECT COUNT(DISTINCT email) FROM customers")
mig_emails = mig.fetchone()[0]
check3_pass = src_emails == mig_emails

# Check 4: Missing records
src.execute("SELECT id FROM customers ORDER BY id")
src_ids = set(row[0] for row in src.fetchall())
mig.execute("SELECT id FROM customers ORDER BY id")
mig_ids = set(row[0] for row in mig.fetchall())
missing_ids = sorted(src_ids - mig_ids)
check4_pass = len(missing_ids) == 0

overall_pass = check1_pass and check2_pass and check3_pass and check4_pass

def status(p):
    return "PASS" if p else "FAIL"

if missing_ids:
    missing_str = ", ".join(str(i) for i in missing_ids)
else:
    missing_str = "none"

overall_str = "PASS" if overall_pass else "FAIL"

report = f"""=== MIGRATION INTEGRITY REPORT ===

[CHECK 1] Row Count
  source: {src_count}
  migrated: {mig_count}
  status: {status(check1_pass)}

[CHECK 2] Balance Sum
  source: {src_balance:.2f}
  migrated: {mig_balance:.2f}
  status: {status(check2_pass)}

[CHECK 3] Email Uniqueness
  source distinct emails: {src_emails}
  migrated distinct emails: {mig_emails}
  status: {status(check3_pass)}

[CHECK 4] Missing Records
  missing IDs: {missing_str}
  status: {status(check4_pass)}

=== OVERALL: {overall_str} ===
"""

with open('/home/user/databases/migration_report.txt', 'w') as f:
    f.write(report)

print("Report written.")
EOF
cat /home/user/databases/migration_report.txt
