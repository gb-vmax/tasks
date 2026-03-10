FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the ETL directory
mkdir -p /home/user/etl

# Create the pipeline.log file with exact contents
cat > /home/user/etl/pipeline.log << 'EOF'
2024-11-01 03:10:01 | ERROR | [EXTRACT] | connection timeout on source DB
2024-11-01 03:10:45 | INFO  | [EXTRACT] | retrying connection, attempt 2 of 3
2024-11-01 03:11:02 | INFO  | [EXTRACT] | source DB connection established
2024-11-01 03:11:30 | WARN  | [TRANSFORM] | column "email" has 12% null rate
2024-11-01 03:12:10 | INFO  | [TRANSFORM] | processing batch 1 of 9
2024-11-01 03:12:45 | ERROR | [TRANSFORM] | null value in non-nullable column "user_id"
2024-11-01 03:13:02 | DEBUG | [TRANSFORM] | row dump: {id: null, email: "a@b.com"}
2024-11-01 03:13:15 | INFO  | [LOAD] | batch 4 of 9 committed successfully
2024-11-01 03:13:50 | WARN  | [VALIDATE] | schema version mismatch, expected v4 got v3
2024-11-01 03:14:02 | ERROR | [LOAD] | deadlock detected on table "events", retrying
2024-11-01 03:14:30 | ERROR | [VALIDATE] | 3 rows failed foreign key constraint on "user_id"
2024-11-01 03:14:55 | INFO  | [LOAD] | batch 7 of 9 committed successfully
2024-11-01 03:15:12 | ERROR | [TRANSFORM] | division by zero in metric "conversion_rate"
2024-11-01 03:15:44 | ERROR | [LOAD] | disk quota exceeded on target warehouse
2024-11-01 03:16:01 | INFO  | [LOAD] | pipeline run completed with errors
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
