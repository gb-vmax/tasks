#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/api_test
cat > /home/user/api_test/response.json <<EOF
{
    "status": "success",
    "code": 200,
    "data": {
        "message": "API call successful"
    }
}
EOF
touch /home/user/api_test/api_test.log
ls -l /home/user/api_test
cat /home/user/api_test/response.json
