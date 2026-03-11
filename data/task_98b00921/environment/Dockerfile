FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

BASE="/home/user/build_env"

# Create directory structure
mkdir -p "$BASE/sdks/android-33"
mkdir -p "$BASE/sdks/android-34"
mkdir -p "$BASE/tools/build-tools-33.0.1"
mkdir -p "$BASE/tools/build-tools-34.0.0"
mkdir -p "$BASE/ndk/ndk-r26b"
mkdir -p "$BASE/java/jdk-17.0.9/bin"

# Create content files
echo "android-33 platform" > "$BASE/sdks/android-33/platform.jar"
echo "android-34 platform" > "$BASE/sdks/android-34/platform.jar"
echo "aapt 33" > "$BASE/tools/build-tools-33.0.1/aapt"
echo "aapt 34" > "$BASE/tools/build-tools-34.0.0/aapt"
echo "ndk-r26b" > "$BASE/ndk/ndk-r26b/ndk-build"
echo "java 17" > "$BASE/java/jdk-17.0.9/bin/java"

# Create broken current-sdk symlink (points to non-existent android-33-gone)
ln -s "android-33-gone" "$BASE/sdks/current-sdk"

# Create build-tools-active symlink pointing to 33.0.1
ln -s "build-tools-33.0.1" "$BASE/tools/build-tools-active"

# Do NOT create: ndk-current, ndk-active, java-home, symlink_manifest.txt

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
