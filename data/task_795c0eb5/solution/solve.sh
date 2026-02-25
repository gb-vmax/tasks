#!/bin/bash
set -e
cd /home/user

python3 -c "
import csv
with open('/home/user/data/sales.csv', newline='', encoding='utf-8') as fin, \
     open('/home/user/data/clean_sales.csv', 'w', newline='', encoding='utf-8') as fout, \
     open('/home/user/data/sales_errors.log', 'w', encoding='utf-8') as ferr:
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    # Read and write the header
    header_line = fin.readline()
    fout.write(header_line)
    # Rewind for correct line tracking
    fin.seek(0)
    next(reader)
    for orig_line in fin:
        try:
            row = next(csv.reader([orig_line]))
            if len(row) == 4:
                writer.writerow(row)
            else:
                ferr.write(orig_line.rstrip('\n') + '\n')
        except Exception:
            ferr.write(orig_line.rstrip('\n') + '\n')
"
cat /home/user/data/clean_sales.csv
cat /home/user/data/sales_errors.log
