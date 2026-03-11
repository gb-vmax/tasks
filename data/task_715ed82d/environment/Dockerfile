FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/mlops/artifact_registry

cat > /home/user/mlops/artifact_registry/VERSION << 'EOF'
1.4.7
EOF

cat > /home/user/mlops/artifact_registry/CHANGELOG.md << 'EOF'
## [1.4.7] - 2024-11-02

### Changed
- Updated feature extraction to use 128-dim embeddings instead of 64-dim

## [1.4.6] - 2024-10-18

### Fixed
- Corrected label encoding for multi-class targets
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
