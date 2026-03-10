FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/logs

cat > /home/user/logs/production.log << 'EOF'
[2024-05-21T08:01:15] [INFO] [api-gateway] Request received from 192.168.1.10
[2024-05-21T08:03:42] [INFO] [auth-service] User login successful for user_id=442
[2024-05-21T08:07:19] [WARN] [db-connector] Slow query detected, took 2300ms
[2024-05-21T08:09:05] [ERROR] [db-connector] Connection pool exhausted ERR-1042
[2024-05-21T08:11:33] [INFO] [payment-service] Transaction initiated tx_id=8821
[2024-05-21T08:15:50] [ERROR] [payment-service] Charge failed for tx_id=8821 ERR-2201
[2024-05-21T08:17:02] [WARN] [api-gateway] Rate limit threshold at 80%
[2024-05-21T08:20:11] [ERROR] [auth-service] Token validation failed ERR-4031
[2024-05-21T08:22:45] [INFO] [db-connector] Index rebuild completed
[2024-05-21T08:25:30] [FATAL] [payment-service] Unrecoverable payment processor error ERR-2201
[2024-05-21T08:27:09] [ERROR] [api-gateway] Upstream timeout ERR-5001
[2024-05-21T08:28:44] [WARN] [auth-service] Failed login attempts exceeded threshold for user_id=107
[2024-05-21T08:30:01] [ERROR] [db-connector] Deadlock detected on table orders ERR-1042
[2024-05-21T08:31:15] [INFO] [api-gateway] Health check passed
[2024-05-21T08:33:22] [FATAL] [db-connector] Disk quota exceeded ERR-9900
[2024-05-21T08:35:48] [ERROR] [payment-service] Duplicate transaction detected ERR-2201
[2024-05-21T08:37:03] [INFO] [auth-service] Session token refreshed for user_id=882
[2024-05-21T08:39:17] [WARN] [db-connector] Replication lag 4500ms
[2024-05-21T08:41:55] [ERROR] [api-gateway] Invalid request signature ERR-4031
[2024-05-21T08:43:20] [INFO] [payment-service] Transaction completed tx_id=9012
[2024-05-21T08:45:08] [WARN] [payment-service] Currency conversion rate stale
[2024-05-21T08:47:33] [ERROR] [auth-service] OAuth provider unreachable ERR-5001
[2024-05-21T08:49:50] [INFO] [db-connector] Backup snapshot created
[2024-05-21T08:51:12] [ERROR] [db-connector] Connection pool exhausted ERR-1042
[2024-05-21T08:53:40] [FATAL] [api-gateway] Worker process crashed ERR-9900
[2024-05-21T08:55:05] [WARN] [auth-service] Certificate expiring in 7 days
[2024-05-21T08:57:29] [ERROR] [payment-service] Charge failed for tx_id=9102 ERR-2201
[2024-05-21T08:59:14] [INFO] [api-gateway] Request received from 192.168.1.55
[2024-05-21T09:01:38] [ERROR] [auth-service] Token validation failed ERR-4031
[2024-05-21T09:03:55] [FATAL] [payment-service] Payment gateway connection lost ERR-5001
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
