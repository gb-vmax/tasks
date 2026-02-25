I have a directory at /home/user/dev_project containing several files: README.md, main.py, utils.py, test_main.py, requirements.txt, and data.csv. I want to automate organizing these files into subdirectories by file type for better project structure. Specifically, create the following subdirectories inside /home/user/dev_project: src, tests, docs, and data. Then, move main.py and utils.py into the src folder, test_main.py into the tests folder, README.md into docs, and data.csv into data. The requirements.txt file should remain in the root of /home/user/dev_project.

After organizing, generate a text log file at /home/user/dev_project/organization_log.txt. This log should list each file that was moved, the original path, and the new path, one entry per line in the following format (with absolute paths):

Moved /home/user/dev_project/<filename> to /home/user/dev_project/<subdir>/<filename>

Please do not include requirements.txt in the logging, since it was not moved. Make sure that the organization_log.txt file contains an entry for each file that has been moved.
