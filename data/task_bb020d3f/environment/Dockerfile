FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create project directories
mkdir -p /home/user/projects/webapp/config
mkdir -p /home/user/projects/dataservice/data
mkdir -p /home/user/backups

# Create webapp files
cat > /home/user/projects/webapp/index.html << 'EOF'
<html><body>Hello World</body></html>
EOF

cat > /home/user/projects/webapp/app.js << 'EOF'
console.log("webapp started");
EOF

cat > /home/user/projects/webapp/config/settings.json << 'EOF'
{"port": 8080, "debug": false}
EOF

# Create dataservice files
cat > /home/user/projects/dataservice/main.py << 'EOF'
print("dataservice started")
EOF

cat > /home/user/projects/dataservice/requirements.txt << 'EOF'
flask==2.0.1
sqlalchemy==1.4.0
EOF

cat > /home/user/projects/dataservice/data/schema.sql << 'EOF'
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);
EOF

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
