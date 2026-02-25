#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/etl
sqlite3 /home/user/etl/employee_data.db ".mode csv" "DROP TABLE IF EXISTS employees;" "CREATE TABLE employees (id INTEGER, name TEXT, department TEXT, salary INTEGER);" ".import /home/user/data/employees.csv employees"
python3 -c "
import csv, sqlite3, os
db_path = '/home/user/etl/employee_data.db'
csv_in = '/home/user/data/employees.csv'
csv_out = '/home/user/etl/engineering_employees.csv'
conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS employees')
cur.execute('CREATE TABLE employees (id INTEGER, name TEXT, department TEXT, salary INTEGER)')
with open(csv_in, newline='') as cf:
    dr = csv.DictReader(cf)
    to_db = [(int(r['id']), r['name'], r['department'], int(r['salary'])) for r in dr]
    cur.executemany('INSERT INTO employees (id, name, department, salary) VALUES (?, ?, ?, ?)', to_db)
conn.commit()
cur.execute(\"SELECT id, name, department, salary FROM employees WHERE department='Engineering' ORDER BY id\")
rows = cur.fetchall()
with open(csv_out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['id','name','department','salary'])
    w.writerows(rows)
conn.close()
"
cat /home/user/etl/engineering_employees.csv
