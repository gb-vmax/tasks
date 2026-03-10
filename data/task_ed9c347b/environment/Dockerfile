FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/project

cat > /home/user/project/build.log << 'EOF'
[INFO] Build started at 2024-03-15 09:00:00
[INFO] Compiling src/main.c
src/main.c:10:5: error: undeclared identifier 'x'
src/main.c:14:3: warning: implicit declaration of function 'printf'
[INFO] Compiling src/auth.c
src/auth.c:42:8: warning: unused variable 'token'
src/auth.c:57:12: note: variable declared here
src/auth.c:61:1: error: expected ';' before '}' token
[INFO] Compiling src/utils.c
src/utils.c:88:1: warning: comparison between signed and unsigned integer expressions
src/utils.c:102:15: warning: format '%d' expects argument of type 'int'
[INFO] Compiling src/config.c
src/config.c:7:4: note: initialized here
src/config.c:19:22: warning: unused parameter 'opts'
[INFO] Build failed with 2 errors and 5 warnings
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
