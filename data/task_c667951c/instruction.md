As a compliance analyst, I need you to verify and document the target destinations of all symbolic links within the directory /home/user/compliance_symlinks. Your task is to generate an audit trail in the form of a plain text file saved at /home/user/symlink_audit.log.

For each symbolic link found directly under /home/user/compliance_symlinks (do not check subdirectories), you must write a line in the log file using the following format:

<symlink name> -> <target path>

For example, if there is a symlink named "conf1" pointing to "/etc/conf/config1.cfg", the output line should be:

conf1 -> /etc/conf/config1.cfg

There should be one entry per symlink, sorted in ascending lexicographical order by the symlink filename. If a symlink points to a path that no longer exists, you must still include that path as the target.

The log file must contain only the audit entries, no extra lines or comments.
