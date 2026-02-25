#!/bin/bash
set -e
cd /home/user

awk -F',' -v OFS=',' 'NR==1 {
    header=$0;
    for (i=1; i<=NF; i++) if ($i=="age") age_idx=i;
    print header > "/home/user/data_pipeline/cleaned_customers.csv";
    next
}
{
    raw=$0;
    # skip blank lines
    if ($0 ~ /^[ \t\r\n]*$/) {
        print raw >> "/home/user/data_pipeline/error_rows.log";
        next
    }
    split($0, fields, FS);
    # check if age field exists
    if (!(age_idx in fields)) {
        print raw >> "/home/user/data_pipeline/error_rows.log";
        next
    }
    age = fields[age_idx];
    # check for non-empty, strictly integer
    if (age == "" || age !~ /^-?[0-9]+$/) {
        print raw >> "/home/user/data_pipeline/error_rows.log";
        next
    }
    print raw >> "/home/user/data_pipeline/cleaned_customers.csv";
}' /home/user/data_pipeline/raw_customers.csv
cat /home/user/data_pipeline/cleaned_customers.csv
cat /home/user/data_pipeline/error_rows.log
