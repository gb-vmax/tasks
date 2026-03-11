FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

BUILDS="/home/user/artifacts/builds"

# Create build version directories with required files
for version in "2.1.0" "2.2.0" "2.3.1"; do
    mkdir -p "$BUILDS/$version"
    touch "$BUILDS/$version/app.tar.gz"
    echo "status=stable" > "$BUILDS/$version/build.meta"
done

mkdir -p "$BUILDS/2.3.0-beta"
touch "$BUILDS/2.3.0-beta/app.tar.gz"
echo "status=beta" > "$BUILDS/2.3.0-beta/build.meta"

# Do NOT create releases/ directory, symlinks, or manifest.txt
# The agent will create those

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
