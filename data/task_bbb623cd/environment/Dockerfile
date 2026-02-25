FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

# Install python3 and pip, then pytest (for testing)
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip
pip3 install --no-cache-dir pytest

# Create the user and home directory if not already present
useradd -m user || true

# Create the db_query_optim directory and set permissions
mkdir -p /home/user/db_query_optim
chown user:user /home/user/db_query_optim
chmod 755 /home/user/db_query_optim

# Create the three SQL template files with the specified content
echo 'SELECT * FROM prod_table;' > /home/user/db_query_optim/query_prod.sql
echo 'SELECT * FROM test_table;' > /home/user/db_query_optim/query_test.sql
echo 'SELECT * FROM dev_table;' > /home/user/db_query_optim/query_dev.sql

# Set ownership and permissions for the SQL files
chown user:user /home/user/db_query_optim/query_prod.sql
chown user:user /home/user/db_query_optim/query_test.sql
chown user:user /home/user/db_query_optim/query_dev.sql
chmod 644 /home/user/db_query_optim/query_prod.sql
chmod 644 /home/user/db_query_optim/query_test.sql
chmod 644 /home/user/db_query_optim/query_dev.sql
ENDPOST

WORKDIR /home/user
