FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the webproject directory
mkdir -p /home/user/webproject

# Create index.html
cat > /home/user/webproject/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head><title>My App</title></head>
<body><h1>Hello World</h1></body>
</html>
EOF

# Create style.css
cat > /home/user/webproject/style.css << 'EOF'
body {
  margin: 0;
  font-family: sans-serif;
  background: #f0f0f0;
}
EOF

# Create app.js
cat > /home/user/webproject/app.js << 'EOF'
document.addEventListener('DOMContentLoaded', function() {
  console.log('App loaded');
});
EOF

# Create dev.config.json
cat > /home/user/webproject/dev.config.json << 'EOF'
{
  "debug": true,
  "api_url": "http://localhost:3000"
}
EOF

# Create notes.txt
cat > /home/user/webproject/notes.txt << 'EOF'
TODO: minify before deploy
check browser compatibility
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
