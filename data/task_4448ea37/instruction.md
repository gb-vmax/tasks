You are a site reliability engineer tasked with monitoring the uptime of the local SSH service (`sshd`). Please perform the following steps:

1. Check the status of the SSH daemon (`sshd`) process and determine whether it is currently running.
2. Save your findings into a log file located at `/home/user/uptime_audit/ssh_status.log`. The log file should use the following format:
   - The first line must be in the form: `Timestamp: YYYY-MM-DD HH:MM:SS`
   - The second line must be either: `sshd status: running` or `sshd status: not running` depending on the result.
   - The timestamp must represent the current system time when you checked the status, in 24-hour format.
3. If the directory `/home/user/uptime_audit` does not exist, you should create it first.
4. Confirm the log file has been properly written by printing its contents to the terminal.

You do not need to change any SSH configuration or start/stop any services—only report the status and log it as specified.
