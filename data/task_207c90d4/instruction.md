As a support engineer, you need to collect diagnostics from a legacy Python script in order to troubleshoot a reported issue. In the directory /home/user/legacy_app, there is an old Python 2 script named collect_info.py.

Your task is as follows:

1. Run the collect_info.py script using Python 2 (the script does not support Python 3). Ensure the script completes without interruption.
2. Redirect all standard output from this script execution to a log file named /home/user/legacy_app/diagnostics.log. If the log file already exists, overwrite its previous contents.
3. Verify the diagnostics log follows this precise output format (which will be checked for testing):  
   - The first line should start with "System Diagnostics Report -", followed by a timestamp in YYYY-MM-DD HH:MM:SS format. For example:  
     System Diagnostics Report - 2023-01-01 13:37:00
   - The next three lines should each begin with one of: "Hostname:", "OS Version:", or "Uptime:". The values after the colons may vary.
   - Any subsequent lines may contain other diagnostics data and can be ignored for the format check.

Make sure to only run the script and collect the output as specified above. Do not modify the script or log file contents directly.
