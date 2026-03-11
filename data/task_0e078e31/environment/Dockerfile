FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/artifacts

# Create JAR files with known content
printf 'JARDATA:core:1.0' > /home/user/artifacts/app-core-1.0.jar
printf 'JARDATA:ui:2.1' > /home/user/artifacts/app-ui-2.1.jar
printf 'JARDATA:utils:1.4' > /home/user/artifacts/app-utils-1.4.jar

# Create correct SHA256 for app-core-1.0.jar
sha256sum /home/user/artifacts/app-core-1.0.jar | cut -d' ' -f1 | tr -d '\n' > /home/user/artifacts/app-core-1.0.sha256

# Create INCORRECT SHA256 for app-ui-2.1.jar (simulating corruption)
printf '0000000000000000000000000000000000000000000000000000000000000000' > /home/user/artifacts/app-ui-2.1.sha256

# Create correct SHA256 for app-utils-1.4.jar
sha256sum /home/user/artifacts/app-utils-1.4.jar | cut -d' ' -f1 | tr -d '\n' > /home/user/artifacts/app-utils-1.4.sha256

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
