You are tasked with hardening a basic data pipeline as a Linux systems engineer. The pipeline copies all ".conf" files from /home/user/source_configs/ to /home/user/hardened_configs/, then appends "# Hardened" at the end of each file in the target directory. Your job also includes robust error recovery: if any ".conf" file fails to copy or append, you must record the exact filename, the step ("copy" or "append"), and the error message in /home/user/hardened_configs/error_log.txt. 

After completion, ensure the following:

1. All ".conf" files originally in /home/user/source_configs/ appear in /home/user/hardened_configs/ and end with a line containing only "# Hardened" (unless an error prevented processing).
2. If errors occurred, /home/user/hardened_configs/error_log.txt exists and follows this strict format (one entry per line): 
   [filename]:[step]:[error_message]
3. If all files are successfully processed with no errors, either do not create error_log.txt or leave it empty.
4. Do not change, delete, or modify any other files or directories.

No additional output is required.
