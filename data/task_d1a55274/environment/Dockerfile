FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the website directory structure
mkdir -p /home/user/projects/website/src
mkdir -p /home/user/projects/website/config

# Create the source files with exact content
cat > /home/user/projects/website/index.html << 'EOF'
<html><body>Hello</body></html>
EOF

cat > /home/user/projects/website/style.css << 'EOF'
body { margin: 0; }
EOF

cat > /home/user/projects/website/src/app.js << 'EOF'
console.log('app');
EOF

cat > /home/user/projects/website/src/utils.js << 'EOF'
function helper() {}
EOF

cat > /home/user/projects/website/config/nginx.conf << 'EOF'
server { listen 80; }
EOF

cat > /home/user/projects/website/config/env.cfg << 'EOF'
ENV=production
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
