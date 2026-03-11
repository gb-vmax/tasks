FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the servers directory
mkdir -p /home/user/servers

# Create the inventory CSV file
cat > /home/user/servers/inventory.csv << 'EOF'
hostname,ip_address,role,status,os
webserver01,10.0.1.5,web,active,Ubuntu
dbserver01,10.0.2.10,database,inactive,CentOS
appserver01,10.0.3.15,application,active,Ubuntu
cacheserver01,10.0.4.20,cache,maintenance,Debian
webserver02,10.0.1.6,web,active,Ubuntu
dbserver02,10.0.2.11,database,active,CentOS
monserver01,10.0.5.30,monitoring,inactive,Debian
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
