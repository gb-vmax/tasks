#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/k8s-manifests/releases/v1 && mv /home/user/k8s-manifests/frontend-deployment.yaml /home/user/k8s-manifests/backend-deployment.yaml /home/user/k8s-manifests/database-deployment.yaml /home/user/k8s-manifests/releases/v1/
ln -sf /home/user/k8s-manifests/releases/v1/frontend-deployment.yaml /home/user/k8s-manifests/current/frontend.yaml && ln -sf /home/user/k8s-manifests/releases/v1/backend-deployment.yaml /home/user/k8s-manifests/current/backend.yaml && ln -sf /home/user/k8s-manifests/releases/v1/database-deployment.yaml /home/user/k8s-manifests/current/database.yaml
cd /home/user/k8s-manifests/current/ && for link in frontend.yaml backend.yaml database.yaml; do target=$(readlink -f "$link"); [ -e "$target" ] && exists=yes || exists=no; echo "$link: $target -> $exists"; done > /home/user/k8s-manifests/link-status.log
cat /home/user/k8s-manifests/link-status.log
