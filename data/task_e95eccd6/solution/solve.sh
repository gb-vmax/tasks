#!/bin/bash
set -e
cd /home/user

echo "id,name,email" > /home/user/db-migration/customers_export.csv && sqlite3 -noheader -separator ',' /home/user/db-migration/source.db "select id,name,email from customers;" >> /home/user/db-migration/customers_export.csv
sqlite3 /home/user/db-migration/target.db ".mode csv" ".import --skip 1 /home/user/db-migration/customers_export.csv customers"
count=$(sqlite3 /home/user/db-migration/target.db "select count(*) from customers;") && read id name email <<< $(sqlite3 /home/user/db-migration/target.db "select id, name, email from customers order by id asc limit 1;") && echo -e "Migrated $count records to target.db\nFirst customer: id=$id, name=$name, email=$email" > /home/user/db-migration/validation.log
cat /home/user/db-migration/validation.log
count=$(sqlite3 /home/user/db-migration/target.db "select count(*) from customers;") && row=$(sqlite3 -separator ',' /home/user/db-migration/target.db "select id, name, email from customers order by id asc limit 1;") && IFS=',' read id name email <<< "$row" && echo -e "Migrated $count records to target.db\nFirst customer: id=$id, name=$name, email=$email" > /home/user/db-migration/validation.log
cat /home/user/db-migration/validation.log
