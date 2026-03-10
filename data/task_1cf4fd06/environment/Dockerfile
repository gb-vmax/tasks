FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/pipeline

cat > /home/user/pipeline/process.sh << 'EOF'
#!/bin/bash
# Simulate a lightweight data processing step
total=0
for i in $(seq 1 5000); do
    total=$((total + i))
done
echo "processed: $total" > /dev/null
EOF

chmod +x /home/user/pipeline/process.sh

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
