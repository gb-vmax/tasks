FROM endless-deps-87d163a8074d:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the project directory
mkdir -p /home/user/migration_project

# Create the install_spec.txt file
cat > /home/user/migration_project/install_spec.txt << 'EOF'
requests==2.28.2
boto3==1.26.90
click==8.1.3
EOF

# Ensure correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
