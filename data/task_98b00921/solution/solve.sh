#!/bin/bash
set -e
cd /home/user

find /home/user/build_env -maxdepth 3 | sort
ls -la /home/user/build_env/sdks/ /home/user/build_env/tools/ /home/user/build_env/ndk/ /home/user/build_env/java/
ln -sfn android-34 /home/user/build_env/sdks/current-sdk
ln -sfn build-tools-34.0.0 /home/user/build_env/tools/build-tools-active
ln -sfn ndk-r26b /home/user/build_env/ndk/ndk-current
ln -s /home/user/build_env/ndk/ndk-r26b /home/user/build_env/tools/ndk-active
ln -sfn jdk-17.0.9 /home/user/build_env/java/java-home
find /home/user/build_env -type l | sort | while read -r link; do
    target=$(readlink "$link")
    if [ -e "$link" ]; then
        status="OK"
    else
        status="BROKEN"
    fi
    echo "$link -> $target [$status]"
done > /home/user/build_env/symlink_manifest.txt
cat /home/user/build_env/symlink_manifest.txt
