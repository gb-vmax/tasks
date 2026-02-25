FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux

# Create user 'user' with home directory /home/user
useradd -m -s /bin/bash user

# Install Python3, pip, sqlite3
apt-get update
apt-get install -y python3 python3-pip sqlite3

# Install pytest
pip3 install pytest

# Create required directories and set permissions
mkdir -p /home/user/data
mkdir -p /home/user/backups
mkdir -p /home/user/backup_logs

# Ensure 'user' owns the directories and they are writable
chown -R user:user /home/user/data /home/user/backups /home/user/backup_logs
chmod 700 /home/user/data /home/user/backups /home/user/backup_logs

# Create the SQLite3 database with 'customers' and 'orders' tables
su - user -c "sqlite3 /home/user/data/customer_data.db \
    \"CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT); \
    CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, amount REAL, \
    FOREIGN KEY(customer_id) REFERENCES customers(id));\""
ENDPOST

WORKDIR /home/user
