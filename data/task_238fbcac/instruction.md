You are a DevOps engineer tasked with quickly identifying error messages related to the "nginx" service from a log file to assist in debugging an issue with the web server. In the file /home/user/logs/nginx_app.log, search for all lines containing the word "ERROR" (case-sensitive). Your task is to output each matching line, preserving their original order, to both the console and into a new file at /home/user/logs/nginx_error_lines.txt.

The output file /home/user/logs/nginx_error_lines.txt must:
- Contain only the complete log lines from /home/user/logs/nginx_app.log that have "ERROR" in them, in the same sequence as in the original file.
- Not include any extra blank lines or leading/trailing spaces.
- Retain the original formatting of the matching lines.

Print each matching line to the console as you write it. The automated test will check that /home/user/logs/nginx_error_lines.txt contains exactly the lines from /home/user/logs/nginx_app.log where "ERROR" appears, with no other content.
