FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/api_test

cat >/home/user/api_test/response.json <<'EOF'
{
    "status": "success",
    "code": 200,
    "data": {
        "message": "API call successful"
    }
}
EOF

: > /home/user/api_test/api_test.log

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
