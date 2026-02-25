As a deployment engineer, you need to apply a simple update process for a web application. 

Start by creating a new directory named <code>/home/user/deployments/v2_1_release/</code>. Next, move all files (not directories) from the existing directory <code>/home/user/webapp_updates/</code> into the new directory you just created.

For verification, generate a log file named <code>/home/user/update_log.txt</code>. The log file must list the names of all files that were moved, one per line, in alphabetical order. The format must be:

<pre>
Moved files:
FILENAME1
FILENAME2
...
</pre>

Replace <code>FILENAME1</code>, <code>FILENAME2</code>, etc. with the actual file names that were moved (do not include any path; just the file name). Only list the files that were moved, and do not include directories or their names. Ensure no extra whitespace or blank lines.
