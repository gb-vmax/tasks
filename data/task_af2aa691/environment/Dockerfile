FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/legacy_tool_a
mkdir -p /home/user/legacy_tool_b

cat > /home/user/legacy_tool_a/tool_a.py <<'EOF'
print("Tool A started")
print("Processing data...")
print("Tool A completed successfully")
EOF

cat > /home/user/legacy_tool_b/tool_b.py <<'EOF'
print("Tool B initiated")
print("Analyzing files...")
print("Tool B finished without errors")
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
