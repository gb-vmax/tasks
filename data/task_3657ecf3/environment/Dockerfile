FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create directory structure
mkdir -p /home/user/backups
mkdir -p /home/user/projects/client_alpha/config

# Create report.txt
cat > /home/user/projects/client_alpha/report.txt << 'EOF'
Q1 Report
Revenue: 50000
Expenses: 32000
EOF

# Create notes.md
cat > /home/user/projects/client_alpha/notes.md << 'EOF'
# Client Alpha Notes

Meeting scheduled for Friday.
EOF

# Create data.csv
cat > /home/user/projects/client_alpha/data.csv << 'EOF'
id,name,value
1,foo,100
2,bar,200
3,baz,300
EOF

# Create config/settings.cfg
cat > /home/user/projects/client_alpha/config/settings.cfg << 'EOF'
[default]
retries=3
timeout=30
EOF

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
