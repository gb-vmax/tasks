FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

WEBAPP="/home/user/webapp"

# Create directory structure
mkdir -p "$WEBAPP/assets/css"
mkdir -p "$WEBAPP/assets/js"
mkdir -p "$WEBAPP/src/components"
mkdir -p "$WEBAPP/src/pages"
mkdir -p "$WEBAPP/src/styles"
mkdir -p "$WEBAPP/logs"
mkdir -p "$WEBAPP/tmp"

# Create HTML files (without deployment marker)
cat > "$WEBAPP/index.html" << 'EOF'
<!DOCTYPE html>
<html><head><title>Home</title></head><body><h1>Hello</h1></body></html>
EOF

cat > "$WEBAPP/about.html" << 'EOF'
<!DOCTYPE html>
<html><head><title>About</title></head><body><h1>About</h1></body></html>
EOF

cat > "$WEBAPP/src/pages/contact.html" << 'EOF'
<!DOCTYPE html>
<html><head><title>Contact</title></head><body><h1>Contact</h1></body></html>
EOF

# Create CSS files
cat > "$WEBAPP/assets/css/main.css" << 'EOF'
body { margin: 0; padding: 0; }
EOF

cat > "$WEBAPP/assets/css/reset.css" << 'EOF'
* { box-sizing: border-box; }
EOF

# Create JS files
cat > "$WEBAPP/assets/js/app.js" << 'EOF'
console.log('app loaded');
EOF

cat > "$WEBAPP/assets/js/vendor.js" << 'EOF'
// vendor bundle
EOF

cat > "$WEBAPP/src/components/widget.js" << 'EOF'
function widget() { return true; }
EOF

# Create theme CSS
cat > "$WEBAPP/src/styles/theme.css" << 'EOF'
:root { --color: #333; }
EOF

# Create log files (uncompressed)
cat > "$WEBAPP/logs/access.log" << 'EOF'
127.0.0.1 GET /index.html 200
127.0.0.1 GET /about.html 200
EOF

cat > "$WEBAPP/logs/error.log" << 'EOF'
ERROR: timeout on /api/data
EOF

# Create stale cache and backup files
cat > "$WEBAPP/tmp/session.cache" << 'EOF'
session_data=abc123
EOF

cat > "$WEBAPP/tmp/query.cache" << 'EOF'
SELECT * FROM users
EOF

cat > "$WEBAPP/tmp/index.html.bak" << 'EOF'
<!DOCTYPE html><html><body>old</body></html>
EOF

cat > "$WEBAPP/src/app.js.bak" << 'EOF'
// old version
EOF

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
