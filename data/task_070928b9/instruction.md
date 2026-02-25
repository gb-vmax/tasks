As part of your role as an observability engineer, you want to quickly check for any world-writable files within the /home/user/logs directory, to ensure there are no security risks involving sensitive log data being improperly exposed. 

Your task is to perform a security scan that lists all world-writable regular files (not directories) present directly or within any subdirectory of /home/user/logs. The output must be saved to a file at /home/user/logs/world_writable_scan.txt.

Each line of the output file must contain the absolute path of a world-writable regular file, one file per line. No additional text, headers, or explanations should be included in the file—just the list of absolute paths. 

For example, if a file called /home/user/logs/app.log is world-writable, it should appear in the output as:
/home/user/logs/app.log

If there are no world-writable files, then /home/user/logs/world_writable_scan.txt should be an empty file.

Please ensure that the scan includes all regular files within /home/user/logs and its subdirectories, and does not list directories, symlinks, or other types of entries.
