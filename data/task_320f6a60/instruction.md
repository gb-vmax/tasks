You are a security auditor tasked with validating the symbolic link structure and file permissions in a user's workspace. Follow these steps to complete the audit:

1. In the directory <code>/home/user/workspace</code>, there are three symbolic links: <code>project_link</code>, <code>config_symlink</code>, and <code>data_link</code>. Each symbolic link points to a different target file:
   - <code>project_link</code> points to <code>/home/user/projects/main_project.txt</code>
   - <code>config_symlink</code> points to <code>/home/user/config/settings.conf</code>
   - <code>data_link</code> points to <code>/home/user/data/raw_dataset.csv</code>
   
   All target files and directories are present.

2. Your task is to:
   - Verify that all three symbolic links exist in <code>/home/user/workspace</code> and point to the correct targets.
   - Check both the symbolic link permissions and the permissions of the target files. Ensure that:
     - Each symbolic link itself has permissions <code>lrwxrwxrwx</code> (symlinks display these permissions).
     - <code>main_project.txt</code> has permissions <code>-rw-------</code>.
     - <code>settings.conf</code> has permissions <code>-rw-r-----</code>.
     - <code>raw_dataset.csv</code> has permissions <code>-rwxr-x---</code>.

3. Produce an audit report named <code>/home/user/audit_report.txt</code> with the following format exactly (with no extra fields, spacing, or missing lines):

<pre>
Symbolic Link Audit Report
--------------------------
project_link: EXISTS, points to /home/user/projects/main_project.txt, perms: lrwxrwxrwx, target perms: -rw-------
config_symlink: EXISTS, points to /home/user/config/settings.conf, perms: lrwxrwxrwx, target perms: -rw-r-----
data_link: EXISTS, points to /home/user/data/raw_dataset.csv, perms: lrwxrwxrwx, target perms: -rwxr-x---
</pre>

Only produce this file with the exact content if the symbolic links and targets match the specification. If there is any discrepancy, instead produce a report at the same location indicating "Audit failed: Discrepancy found in symbolic links or permissions."" Do not add any other output to the file.

Finish by printing the content of <code>/home/user/audit_report.txt</code> to the console.
