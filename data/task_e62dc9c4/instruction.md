You are an MLOps engineer in charge of tracking experiment artifacts for a machine learning project. You recently discovered that the artifacts directory, located at /home/user/mlops_artifacts/, has global write permissions, which is a security vulnerability because any user can potentially modify or delete experiment results. Your task is to fix this issue by ensuring that only the current user (user) has write access to /home/user/mlops_artifacts/, and that all files and subdirectories within it are updated accordingly.

After making this change, generate a plain text verification report named /home/user/artifact_permission_fix.log in the following format:

Directory: /home/user/mlops_artifacts/
Writable by group: <yes|no>
Writable by others: <yes|no>
All files and subdirectories now writable only by owner: <yes|no>

The test system will verify this log file. Confirm there are no remaining group or others write permissions on the directory or its contents.
