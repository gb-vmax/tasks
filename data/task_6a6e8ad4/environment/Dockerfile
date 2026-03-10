FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/admin

cat > /home/user/admin/users.csv << 'EOF'
username,email,role,status
alice,alice@example.com,admin,active
bob,bob@example.com,editor,inactive
carol,carol@example.com,viewer,active
dave,dave@example.com,admin,inactive
eve,eve@example.com,editor,active
frank,frank@example.com,admin,active
grace,grace@example.com,viewer,inactive
heidi,heidi@example.com,editor,active
ivan,ivan@example.com,viewer,active
judy,judy@example.com,admin,inactive
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
