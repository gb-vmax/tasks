You are managing containerized microservices and need to back up and verify logs from two services. In the /home/user/microservices directory, you will find two subdirectories: /home/user/microservices/auth and /home/user/microservices/payment. Each contains a log file: /home/user/microservices/auth/auth.log and /home/user/microservices/payment/payment.log.

Your task:
1. Compress both log files into a single tar.gz archive named /home/user/logs_backup.tar.gz. The archive should contain only the two log files (not the directories), and they should appear at the root of the archive as auth.log and payment.log.
2. Extract the contents of /home/user/logs_backup.tar.gz into a new directory named /home/user/logs_restore.
3. After extraction, create a report file at /home/user/logs_restore/restore_report.txt with the following format:

Restored Files:
<list all extracted files on separate lines>

Sample contents:
Restored Files:
auth.log
payment.log

Be sure to maintain this exact output format, with the list of files matching the names of the extracted files in /home/user/logs_restore.
