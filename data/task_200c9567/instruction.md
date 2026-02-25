As a deployment engineer, you need to roll out updates to the "analytics-app" deployment environment located in /home/user/deployments/analytics-app. Your tasks are as follows:

1. Check if the directory /home/user/deployments/analytics-app exists. If not, create it and ensure it is owned by the user.
2. Update or create the .env file at /home/user/deployments/analytics-app/.env. This file should contain the following lines, replacing any previous values for the keys if they exist:
   - APP_VERSION=3.8.2
   - DATABASE_URL=postgresql://analytics:Password123@db.internal:5432/analyticsdb
   - ENABLE_CACHE=true
   - LOG_LEVEL=info
   - DEPLOY_TIMESTAMP=(current UTC date and time in ISO 8601 format, e.g., 2023-05-17T11:32:24Z)
3. In the same directory, create a deployment log file named deploy.log, which must contain a single line recording the new deployment. The line must follow this format:
   [DEPLOYED] <ISO8601 timestamp> - version 3.8.2 deployed by user
   For example:
   [DEPLOYED] 2024-06-12T12:15:00Z - version 3.8.2 deployed by user
   The ISO8601 timestamp must exactly match the value used for DEPLOY_TIMESTAMP in the .env file.
4. Ensure that after completing these actions, both .env and deploy.log are readable and writable by user, but not executable.
5. Print to the terminal the contents of the new .env file, the full path to deploy.log, and the contents of the deploy.log file in that order. The output should be unadorned text, without extra messages.

The automated test will verify the presence, content, and permissions of both files and compare your terminal output exactly as specified above.
