FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/pipeline

cat > /home/user/pipeline/build.ini << 'EOF'
; Mobile build pipeline configuration
; Managed by the CI team

[project]
app_name = FluxMobile
version_name = 3.7.2
version_code = 4109
build_date = 2024-11-01

[android]
build_type = release
min_sdk = 24
target_sdk = 34
keystore_file = /etc/ci/release.keystore
sign_config = production

[ios]
scheme = FluxMobile-Prod
deployment_target = 15.0
provisioning_profile = match_appstore_com.flux.mobile
code_sign_identity = iPhone Distribution

[notifications]
slack_channel = #mobile-builds
email = builds@flux.io
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
