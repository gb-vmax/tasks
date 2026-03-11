FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the artifacts and build directories
mkdir -p /home/user/artifacts/build

# Create app.js
cat > /home/user/artifacts/build/app.js << 'EOF'
function greet(name) {
    return "Hello, " + name + "!";
}
function add(a, b) {
    return a + b;
}
function subtract(a, b) {
    return a - b;
}
function multiply(a, b) {
    return a * b;
}
function divide(a, b) {
    if (b === 0) throw new Error("division by zero");
    return a / b;
}
console.log(greet("world"));
console.log(add(1, 2));
console.log(subtract(10, 4));
console.log(multiply(3, 7));
console.log(divide(20, 5));
EOF

# Create styles.css
cat > /home/user/artifacts/build/styles.css << 'EOF'
body { margin: 0; padding: 0; font-family: sans-serif; background: #fff; color: #333; }
h1 { font-size: 2em; font-weight: bold; margin-bottom: 0.5em; }
h2 { font-size: 1.5em; font-weight: bold; margin-bottom: 0.4em; }
p { line-height: 1.6; margin-bottom: 1em; }
a { color: #0066cc; text-decoration: none; }
a:hover { text-decoration: underline; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 1em; }
.header { background: #333; color: #fff; padding: 1em 0; }
.footer { background: #f5f5f5; border-top: 1px solid #ddd; padding: 1em 0; text-align: center; }
EOF

# Create manifest.json
cat > /home/user/artifacts/build/manifest.json << 'EOF'
{
  "name": "my-app",
  "version": "2.4.1",
  "build": "20240315",
  "files": ["app.js", "styles.css", "manifest.json"],
  "checksums": {
    "app.js": "abc123def456",
    "styles.css": "789xyz012uvw",
    "manifest.json": "qrs345tuv678"
  },
  "target": "production",
  "minified": false,
  "sourceMaps": false
}
EOF

# Set ownership
chown -R user:user /home/user
EOF
ENDSETUP

WORKDIR /home/user
