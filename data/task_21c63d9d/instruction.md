As a release manager, you need to prepare a simple data pipeline to process deployment artifacts. In the directory /home/user/deployment_staging, there are two files: app.tar.gz and readme.txt. Your tasks are as follows:

1. Move app.tar.gz to the /home/user/deployment_ready directory. 
2. If the move is successful, write "SUCCESS: app.tar.gz moved to deployment_ready" to a log file called /home/user/deployment_logs/pipeline.log. 
3. If the move fails for any reason, write "ERROR: app.tar.gz could not be moved" to the same log file.

The log file /home/user/deployment_logs/pipeline.log should contain exactly one line, according to the above logic. The log line should be plain ASCII text with no timestamps or extra formatting, and the only possible values are as described.

Please ensure that only app.tar.gz is moved and logged; readme.txt should remain in /home/user/deployment_staging.

The automated tests will verify the precise content of /home/user/deployment_logs/pipeline.log and the presence or absence of app.tar.gz in both directories.
