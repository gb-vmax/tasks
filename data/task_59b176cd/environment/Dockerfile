FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create operator directory
mkdir -p /home/user/operator

# Create VERSION file with exactly "1.3.2" (no trailing newline)
printf '1.3.2' > /home/user/operator/VERSION

# Create pending_commits.txt
cat > /home/user/operator/pending_commits.txt << 'EOF'
feat: add leader election support
fix: handle nil pointer in reconcile loop
fix: correct RBAC permissions for CRD watcher
feat: support multi-namespace watch mode
EOF

# Create CHANGELOG.md with exact content
cat > /home/user/operator/CHANGELOG.md << 'EOF'
## [1.3.2] - 2024-10-20

### Changed
- fix: retry on transient API errors
- fix: bump controller-runtime to v0.16.1

---
## [1.3.1] - 2024-09-14

### Changed
- fix: correct status subresource patch logic

---
## [1.3.0] - 2024-09-01

### Changed
- feat: add finalizer support for cleanup on deletion
- fix: resolve race condition in cache sync

---
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
