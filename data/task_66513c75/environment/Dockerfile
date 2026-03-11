FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the base directory
mkdir -p /home/user/k8s-operator

# Create the pre-existing manifest files with exact content
cat > /home/user/k8s-operator/cache-crd.yaml << 'EOF'
kind: CustomResourceDefinition
name: caches
EOF

cat > /home/user/k8s-operator/index-crd.yaml << 'EOF'
kind: CustomResourceDefinition
name: indexes
EOF

cat > /home/user/k8s-operator/operator-role.yaml << 'EOF'
kind: Role
name: operator-role
EOF

cat > /home/user/k8s-operator/operator-rolebinding.yaml << 'EOF'
kind: RoleBinding
name: operator-rolebinding
EOF

cat > /home/user/k8s-operator/operator-deploy.yaml << 'EOF'
kind: Deployment
name: operator
EOF

cat > /home/user/k8s-operator/operator-svc.yaml << 'EOF'
kind: Service
name: operator-svc
EOF

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
