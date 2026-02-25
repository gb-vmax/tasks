#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/provisioned_web
echo '<html>
<body>
<h1>Provisioned Service Ready</h1>
</body>
</html>' > /home/user/provisioned_web/index.html
nohup python3 -m http.server 8080 --directory /home/user/provisioned_web > /home/user/provisioned_web/server.log 2>&1 &
(cd /home/user/provisioned_web && nohup python3 -m http.server 8080 > server.log 2>&1 &)
curl -i http://localhost:8080/ > /home/user/provisioned_web/provision_check.log
cat /home/user/provisioned_web/provision_check.log
