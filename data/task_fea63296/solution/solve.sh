#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/build_artifacts/android /home/user/build_artifacts/ios
find /home/user -type d \( -name android_old -o -name ios_old \)
find /home/user/android_old -mindepth 1 -maxdepth 1
ls -1 /home/user/build_artifacts/android
mv /home/user/android_old/* /home/user/build_artifacts/android/
find /home/user/some/other/path/ios_old -mindepth 1 -maxdepth 1
ls -1 /home/user/build_artifacts/ios
mv /home/user/some/other/path/ios_old/* /home/user/build_artifacts/ios/
rmdir /home/user/android_old /home/user/some/other/path/ios_old
(find /home/user/build_artifacts/android /home/user/build_artifacts/ios -type f | sort && echo "Android files: $(find /home/user/build_artifacts/android -type f | wc -l)" && echo "iOS files: $(find /home/user/build_artifacts/ios -type f | wc -l)") > /home/user/build_artifacts/artifact_report.log
cat /home/user/build_artifacts/artifact_report.log
chown -R user:user /home/user/build_artifacts && find /home/user/build_artifacts -type d -exec chmod 700 {} \; && find /home/user/build_artifacts -type f -exec chmod 600 {} \;
