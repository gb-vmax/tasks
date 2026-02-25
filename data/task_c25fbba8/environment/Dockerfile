FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
# Do NOT run the solution or create output files

BASE="/home/user/app/logs"

# Create directories
mkdir -p "$BASE/server1"
mkdir -p "$BASE/server2"
mkdir -p "$BASE/api"

# Create server1/server.log (modified 9 days ago)
cat > "$BASE/server1/server.log" <<EOF
Line 1
ERROR: Out of memory
Line 3
Line 4
ERROR: Connection lost
ERROR: Disk full
EOF

# Create server2/current.log (modified 3 days ago)
cat > "$BASE/server2/current.log" <<EOF
ERROR: Timeout
Line A
EOF

# Create api/debug.log (modified 12 days ago)
cat > "$BASE/api/debug.log" <<EOF
Debug start
Debug message
Another line
EOF

# Create app.log (modified 15 days ago)
cat > "$BASE/app.log" <<EOF
Something happened
ERROR: Critical failure
Operation complete
ERROR: Unhandled exception
EOF

# Create README.txt (modified 20 days ago)
echo "This is a log directory. Do not delete." > "$BASE/README.txt"

# Set mtimes as required (allow 1 hour slack: set to now - N days + 10 minutes)
now=$(date +%s)

touch -d "@$((now - 9*86400 + 600))" "$BASE/server1/server.log"
touch -d "@$((now - 3*86400 + 600))" "$BASE/server2/current.log"
touch -d "@$((now - 12*86400 + 600))" "$BASE/api/debug.log"
touch -d "@$((now - 15*86400 + 600))" "$BASE/app.log"
touch -d "@$((now - 20*86400 + 600))" "$BASE/README.txt"

# Set permissions: ensure user can read/write everything
chown -R user:user /home/user
chmod -R u+rwX /home/user/app

# Do NOT create /home/user/error_log_summary.txt
ENDSETUP

WORKDIR /home/user
