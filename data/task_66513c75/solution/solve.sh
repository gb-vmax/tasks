#!/bin/bash
set -e
cd /home/user

ls -la /home/user/k8s-operator/
mkdir -p /home/user/k8s-operator/crds /home/user/k8s-operator/rbac /home/user/k8s-operator/deploy
mv /home/user/k8s-operator/cache-crd.yaml /home/user/k8s-operator/crds/ && mv /home/user/k8s-operator/index-crd.yaml /home/user/k8s-operator/crds/ && mv /home/user/k8s-operator/operator-role.yaml /home/user/k8s-operator/rbac/ && mv /home/user/k8s-operator/operator-rolebinding.yaml /home/user/k8s-operator/rbac/ && mv /home/user/k8s-operator/operator-deploy.yaml /home/user/k8s-operator/deploy/ && mv /home/user/k8s-operator/operator-svc.yaml /home/user/k8s-operator/deploy/
chmod 755 /home/user/k8s-operator/crds && chmod 644 /home/user/k8s-operator/crds/*.yaml && chmod 750 /home/user/k8s-operator/rbac && chmod 640 /home/user/k8s-operator/rbac/*.yaml && chmod 750 /home/user/k8s-operator/deploy && chmod 640 /home/user/k8s-operator/deploy/*.yaml
stat --format="%A %n" /home/user/k8s-operator/crds /home/user/k8s-operator/crds/*.yaml /home/user/k8s-operator/deploy /home/user/k8s-operator/deploy/*.yaml /home/user/k8s-operator/rbac /home/user/k8s-operator/rbac/*.yaml | sort -k2 > /home/user/k8s-operator/permissions.txt
cat /home/user/k8s-operator/permissions.txt
ls -la /home/user/k8s-operator/ && echo "---" && ls -la /home/user/k8s-operator/crds/ && echo "---" && ls -la /home/user/k8s-operator/rbac/ && echo "---" && ls -la /home/user/k8s-operator/deploy/
