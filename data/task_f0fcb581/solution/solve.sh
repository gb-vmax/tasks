#!/bin/bash
set -e
cd /home/user

ls /home/user/artifacts/
ls /home/user/artifacts/builds/
for d in /home/user/artifacts/builds/*/; do echo "=== $d ==="; cat "$d/build.meta"; done
mkdir -p /home/user/artifacts/releases
for d in /home/user/artifacts/builds/*/; do version=$(basename "$d"); ln -s "/home/user/artifacts/builds/$version" "/home/user/artifacts/releases/$version"; done
ln -s /home/user/artifacts/builds/2.3.1 /home/user/artifacts/releases/current
ln -s /home/user/artifacts/releases/current /home/user/artifacts/latest-stable
ln -s /home/user/artifacts/builds/2.3.0-beta /home/user/artifacts/latest-beta
ls -la /home/user/artifacts/releases/ && echo "---" && ls -la /home/user/artifacts/latest-stable /home/user/artifacts/latest-beta
DATE=$(date +%Y-%m-%d)

# Build [releases] section in semantic version order
RELEASES_SECTION=""
for version in $(ls /home/user/artifacts/releases/ | grep -v '^current$' | sort -V); do
    target=$(readlink "/home/user/artifacts/releases/$version")
    RELEASES_SECTION="${RELEASES_SECTION}${version}: ${target}\n"
done

# [special] section
CURRENT_TARGET=$(readlink /home/user/artifacts/releases/current)
LATEST_STABLE_TARGET=$(readlink /home/user/artifacts/latest-stable)
LATEST_BETA_TARGET=$(readlink /home/user/artifacts/latest-beta)

# [resolution] section
LATEST_STABLE_REAL=$(realpath /home/user/artifacts/latest-stable)
LATEST_BETA_REAL=$(realpath /home/user/artifacts/latest-beta)

cat > /home/user/artifacts/manifest.txt << EOF
=== ARTIFACT MANIFEST ===
generated: ${DATE}

[releases]
$(printf "$RELEASES_SECTION" | sed '/^$/d')

[special]
current -> ${CURRENT_TARGET}
latest-stable -> ${LATEST_STABLE_TARGET}
latest-beta -> ${LATEST_BETA_TARGET}

[resolution]
latest-stable resolves to: ${LATEST_STABLE_REAL}
latest-beta resolves to: ${LATEST_BETA_REAL}
EOF
cat /home/user/artifacts/manifest.txt
echo "=== releases/ ===" && ls -la /home/user/artifacts/releases/ && echo && echo "=== top-level symlinks ===" && ls -la /home/user/artifacts/latest-stable /home/user/artifacts/latest-beta && echo && echo "=== manifest.txt ===" && cat /home/user/artifacts/manifest.txt
