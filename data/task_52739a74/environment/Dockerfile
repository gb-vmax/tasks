FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/api_diagnostics

# Create auth_events.log
cat > /home/user/api_diagnostics/auth_events.log << 'EOF'
[2024-05-01T10:00:01Z] [INFO] [LOGIN] user=alice result=OK
[2024-05-01T10:00:03Z] [INFO] [LOGIN] user=bob result=FAIL
[2024-05-01T10:00:07Z] [INFO] [LOGIN] user=alice result=OK
[2024-05-01T10:00:12Z] [WARN] [LOGIN] user=charlie result=FAIL
[2024-05-01T10:00:15Z] [INFO] [LOGIN] user=bob result=FAIL
[2024-05-01T10:00:19Z] [INFO] [LOGIN] user=alice result=OK
[2024-05-01T10:00:23Z] [WARN] [LOGIN] user=dave result=FAIL
[2024-05-01T10:00:28Z] [INFO] [LOGIN] user=bob result=OK
[2024-05-01T10:00:31Z] [WARN] [LOGIN] user=charlie result=FAIL
[2024-05-01T10:00:35Z] [INFO] [LOGIN] user=alice result=OK
[2024-05-01T10:00:40Z] [WARN] [LOGIN] user=bob result=FAIL
[2024-05-01T10:00:44Z] [INFO] [LOGIN] user=dave result=OK
[2024-05-01T10:00:48Z] [WARN] [LOGIN] user=charlie result=FAIL
[2024-05-01T10:00:52Z] [INFO] [LOGIN] user=alice result=OK
[2024-05-01T10:00:56Z] [WARN] [LOGIN] user=bob result=FAIL
EOF

# Create latency_samples.csv
cat > /home/user/api_diagnostics/latency_samples.csv << 'EOF'
request_id,endpoint,latency_ms,status_code
req001,/api/users,120,200
req002,/api/orders,450,200
req003,/api/users,95,200
req004,/api/products,870,500
req005,/api/orders,310,200
req006,/api/auth,55,200
req007,/api/products,940,200
req008,/api/users,200,404
req009,/api/auth,80,200
req010,/api/orders,620,200
req011,/api/products,1100,500
req012,/api/auth,45,200
req013,/api/users,175,200
req014,/api/orders,380,200
req015,/api/products,990,200
EOF

# Create error_counts.tsv (tab-separated)
printf '2024-05-01T10:00Z\t/api/users\t3\n' > /home/user/api_diagnostics/error_counts.tsv
printf '2024-05-01T10:00Z\t/api/orders\t7\n' >> /home/user/api_diagnostics/error_counts.tsv
printf '2024-05-01T10:00Z\t/api/products\t12\n' >> /home/user/api_diagnostics/error_counts.tsv
printf '2024-05-01T10:01Z\t/api/users\t5\n' >> /home/user/api_diagnostics/error_counts.tsv
printf '2024-05-01T10:01Z\t/api/orders\t9\n' >> /home/user/api_diagnostics/error_counts.tsv
printf '2024-05-01T10:01Z\t/api/products\t6\n' >> /home/user/api_diagnostics/error_counts.tsv
printf '2024-05-01T10:02Z\t/api/users\t2\n' >> /home/user/api_diagnostics/error_counts.tsv
printf '2024-05-01T10:02Z\t/api/orders\t14\n' >> /home/user/api_diagnostics/error_counts.tsv
printf '2024-05-01T10:02Z\t/api/products\t8\n' >> /home/user/api_diagnostics/error_counts.tsv
printf '2024-05-01T10:03Z\t/api/users\t11\n' >> /home/user/api_diagnostics/error_counts.tsv
printf '2024-05-01T10:03Z\t/api/orders\t4\n' >> /home/user/api_diagnostics/error_counts.tsv
printf '2024-05-01T10:03Z\t/api/products\t3\n' >> /home/user/api_diagnostics/error_counts.tsv

# Create system_metrics.log
cat > /home/user/api_diagnostics/system_metrics.log << 'EOF'
2024-05-01T10:00:00Z cpu_pct=45.2 mem_pct=62.1
2024-05-01T10:00:10Z cpu_pct=72.8 mem_pct=63.4
2024-05-01T10:00:20Z cpu_pct=88.5 mem_pct=65.0
2024-05-01T10:00:30Z cpu_pct=91.3 mem_pct=67.8
2024-05-01T10:00:40Z cpu_pct=79.6 mem_pct=70.2
2024-05-01T10:00:50Z cpu_pct=84.1 mem_pct=72.5
2024-05-01T10:01:00Z cpu_pct=55.3 mem_pct=74.0
2024-05-01T10:01:10Z cpu_pct=63.7 mem_pct=73.1
2024-05-01T10:01:20Z cpu_pct=81.9 mem_pct=75.6
2024-05-01T10:01:30Z cpu_pct=77.4 mem_pct=76.3
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
