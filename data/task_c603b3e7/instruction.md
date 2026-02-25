You are a system administrator tasked with verifying if an old Python script, located at /home/user/legacy_tools/cleanup_temp_files.py, still runs correctly on the current system. This script is supposed to delete all .tmp files from the /home/user/legacy_data directory and print a summary report.

Your task is as follows:

1. Inspect the script at /home/user/legacy_tools/cleanup_temp_files.py and ensure it is Python 2 compatible (i.e., uses code that works with `python2`).
2. Execute the script using Python 2, explicitly calling `python2` (as python3 is also installed on this system).
3. Before running the script, ensure the /home/user/legacy_data directory contains exactly three .tmp files: temp1.tmp, temp2.tmp, temp3.tmp; and two non-tmp files: keepme.txt, archive.log. Do NOT remove or modify non-tmp files.
4. After running the script, confirm that all .tmp files have been deleted from /home/user/legacy_data and non-tmp files remain untouched.
5. The script prints its output report to standard out. Capture this output and save it verbatim into a log file called /home/user/legacy_run/reports/cleanup_YYYYMMDD_HHMMSS.log, where YYYYMMDD_HHMMSS is the script run's timestamp in UTC (use the exact format).
6. The output format of the summary MUST be (with exact spacing, line breaks, and wording):

Cleanup Summary:
Deleted files:
- temp1.tmp
- temp2.tmp
- temp3.tmp
Operation completed successfully.

7. After saving the output, display the absolute path to the generated log file on the console (stdout).
8. Ensure that the permissions of the report log file allow only the current user (read and write, no group/other access: 600).

To verify correctness, the automated test will check:
- All .tmp files are deleted, and non-tmp files remain in /home/user/legacy_data.
- The log file exists at /home/user/legacy_run/reports/ with the correct timestamp format in the filename.
- The contents of the log file exactly match the specified output format.
- Log file has correct permissions (600: user read/write only).
