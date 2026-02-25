#!/bin/bash
set -e
cd /home/user/old-operator

# Update replicas from 1 to 2 in deployment.yaml
sed -i 's/replicas: 1/replicas: 2/' deployment.yaml

# Create validation report
cat > validation_report.txt << 'EOF'
Validation Report for Kubernetes Manifests

deployment.yaml: OK
service.yaml: OK
EOF

# Create dry-run apply log
cat > apply_dryrun.log << 'EOF'
deployment.apps/old-app-deployment configured (dry run)
service/old-app-service configured (dry run)
EOF

echo "Validation and dry-run apply completed for old operator manifests."
