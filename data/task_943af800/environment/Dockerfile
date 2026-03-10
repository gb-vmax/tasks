FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/logs

cat > /home/user/logs/service_errors.csv << 'EOF'
timestamp,service,level,error_code,response_time_ms,region
2024-04-10 08:03:11,auth,ERROR,5001,320,us-east
2024-04-10 08:15:42,auth,ERROR,5001,415,us-east
2024-04-10 08:47:09,payments,ERROR,6002,890,us-west
2024-04-10 09:01:55,auth,INFO,0,98,us-east
2024-04-10 09:12:30,payments,ERROR,6001,1200,us-west
2024-04-10 09:23:44,gateway,WARN,0,250,eu-central
2024-04-10 09:34:01,auth,ERROR,5002,530,us-east
2024-04-10 09:55:17,gateway,ERROR,7001,440,eu-central
2024-04-10 10:02:48,payments,INFO,0,300,us-west
2024-04-10 10:11:59,auth,WARN,0,180,us-east
2024-04-10 10:22:33,gateway,ERROR,7002,670,eu-central
2024-04-10 10:33:07,payments,ERROR,6002,950,us-west
2024-04-10 10:44:21,auth,ERROR,5003,720,us-east
2024-04-10 10:55:50,gateway,INFO,0,120,eu-central
2024-04-10 11:04:13,inventory,ERROR,8001,840,us-east
2024-04-10 11:15:38,inventory,ERROR,8002,760,us-east
2024-04-10 11:26:55,payments,WARN,0,200,us-west
2024-04-10 11:37:44,auth,ERROR,5001,390,us-east
2024-04-10 11:48:02,inventory,ERROR,8001,910,us-west
2024-04-10 11:59:19,gateway,ERROR,7001,510,eu-central
2024-04-10 12:05:33,auth,INFO,0,88,us-east
2024-04-10 12:16:47,payments,ERROR,6003,1100,us-west
2024-04-10 12:27:08,inventory,INFO,0,140,us-east
2024-04-10 12:38:29,gateway,WARN,0,310,eu-central
2024-04-10 12:49:51,auth,ERROR,5002,600,us-east
2024-04-10 13:01:14,payments,ERROR,6001,980,us-west
2024-04-10 13:12:35,inventory,ERROR,8003,700,us-west
2024-04-10 13:23:50,auth,WARN,0,160,us-east
2024-04-10 13:34:07,gateway,ERROR,7003,580,eu-central
2024-04-10 13:45:22,payments,INFO,0,270,us-west
2024-04-10 14:06:41,auth,ERROR,5001,450,us-east
2024-04-10 14:17:58,inventory,WARN,0,130,us-east
2024-04-10 14:29:03,gateway,ERROR,7001,490,eu-central
2024-04-10 14:40:17,payments,ERROR,6002,1050,us-west
2024-04-10 14:51:32,auth,INFO,0,75,us-east
2024-04-10 15:02:49,inventory,ERROR,8001,880,us-east
2024-04-10 15:13:04,gateway,INFO,0,200,eu-central
2024-04-10 15:24:19,payments,WARN,0,190,us-west
2024-04-10 15:35:44,auth,ERROR,5003,680,us-east
2024-04-10 15:46:58,inventory,ERROR,8002,740,us-west
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
