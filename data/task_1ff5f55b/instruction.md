You are a network engineer troubleshooting a connectivity issue on a Linux system. There is a network diagnostic script located at <code>/home/user/tools/ping_test.sh</code> which outputs to a log file <code>/home/user/tools/ping_output.log</code>. For easier access, you need to manage symbolic links in your home directory as follows:

1. Create a symbolic link named <code>/home/user/pingtest</code> that points to <code>/home/user/tools/ping_test.sh</code>.
2. Create a symbolic link named <code>/home/user/pinglog</code> that points to <code>/home/user/tools/ping_output.log</code>.
3. List all symbolic links in <code>/home/user</code> (not subdirectories), displaying the target of each link, and output the result to a log file named <code>/home/user/symlink_report.log</code>. The output in <code>symlink_report.log</code> must exactly follow this format, with one line per link:
<pre>
[symlink_name] -> [target_path]
</pre>
For example:
<pre>
pingtest -> /home/user/tools/ping_test.sh
pinglog -> /home/user/tools/ping_output.log
</pre>
The order of lines does not matter. Ensure that only symbolic links located directly in <code>/home/user</code> are included—do not include symlinks from subdirectories.

This scenario will help you demonstrate proper management of symbolic links and verification of their targets. Let me know when each step is complete by showing console output.
