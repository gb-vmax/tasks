FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

mkdir -p /home/user/k8s-manifests

cat > /home/user/k8s-manifests/deployment.yaml <<'EOF'
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  selector:
    matchLabels:
      app: my-app
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: another-app
spec:
  selector:
    matchLabels:
      app: another-app
EOF

cat > /home/user/k8s-manifests/service.yaml <<'EOF'
---
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
---
apiVersion: v1
kind: Service
metadata:
  name: another-service
spec:
  selector:
    app: another-app
EOF

cat > /home/user/k8s-manifests/configmap.yaml <<'EOF'
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-config
EOF

# Do NOT create kind_frequency.log or any other files.

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
