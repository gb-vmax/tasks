FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the CI directory
mkdir -p /home/user/ci

# Create the pipeline timings log file
cat > /home/user/ci/pipeline_timings.log << 'EOF'
checkout 18
install_deps 47
lint 31
unit_tests 143
build 112
integration_tests 98
package 23
deploy_staging 55
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
