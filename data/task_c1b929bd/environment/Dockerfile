FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create directory structure
mkdir -p /home/user/k8s/operators/cert-manager
mkdir -p /home/user/k8s/operators/prometheus
mkdir -p /home/user/k8s/operators/nginx-ingress

# Create cert-manager/cert-manager.yaml
cat > /home/user/k8s/operators/cert-manager/cert-manager.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cert-manager
  namespace: cert-manager
EOF

# Create cert-manager/webhook.yaml
cat > /home/user/k8s/operators/cert-manager/webhook.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cert-manager-webhook
  namespace: cert-manager
EOF

# Create prometheus/operator.yaml
cat > /home/user/k8s/operators/prometheus/operator.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus-operator
  namespace: monitoring
EOF

# Create prometheus/rbac.yaml
cat > /home/user/k8s/operators/prometheus/rbac.yaml << 'EOF'
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: prometheus-operator
EOF

# Create nginx-ingress/ingress-controller.yaml
cat > /home/user/k8s/operators/nginx-ingress/ingress-controller.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-ingress-controller
  namespace: ingress-nginx
EOF

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
