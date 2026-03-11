FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

cat > /home/user/db_config.ini << 'EOF'
[connection]
host = db.internal.example.com
port = 5432
username = app_user
password = s3cr3tpassw0rd
database = production_db

[performance]
max_connections = 150
query_timeout = 30
cache_size = 512MB
work_mem = 64MB
shared_buffers = 256MB

[logging]
slow_query_log = enabled
slow_query_threshold = 1000
log_level = warning
log_file = /var/log/postgres/queries.log

[replication]
enabled = true
replica_host = replica.internal.example.com
replica_port = 5432
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
