As part of automating infrastructure provisioning, set up a simple HTTP service using Python's built-in HTTP server module and configure it to run in the background on port 8080. You need to:

1. Create a directory at /home/user/provisioned_web.
2. Place an index.html file in /home/user/provisioned_web with the following exact content:
   <html>
   <body>
   <h1>Provisioned Service Ready</h1>
   </body>
   </html>
3. Launch a Python HTTP server from within /home/user/provisioned_web so it listens on port 8080 and runs in the background, logging output to /home/user/provisioned_web/server.log.
4. After launching the server, verify it is running and serving index.html by making an HTTP request (using curl or similar) to http://localhost:8080 and storing the full response (headers and body) in /home/user/provisioned_web/provision_check.log.

Your final step is to ensure that /home/user/provisioned_web/provision_check.log contains both the HTTP headers and the HTML content of index.html as served by your running HTTP server. 

You do not need to stop the server once the log is created. The test will check for the precise presence and contents of:
- /home/user/provisioned_web/index.html
- /home/user/provisioned_web/server.log
- /home/user/provisioned_web/provision_check.log (must show correct headers and HTML)
