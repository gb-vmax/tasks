You are acting as a storage administrator who needs to quickly check the free disk space thresholds for specific mount points as defined in a configuration file. You are given an INI file located at <code>/home/user/storage/config.ini</code> which includes disk monitoring thresholds for different mount points under a <code>[disk_thresholds]</code> section. 

Your task is to read this INI configuration file, extract the free space warning thresholds for the mount points <code>/data1</code> and <code>/backup</code>, and write them into a summary file named <code>/home/user/storage/threshold_summary.txt</code>. 

In the summary file, print each threshold on its own line in the following explicit format (including spacing and punctuation):

<pre>
/data1: THRESHOLD_VALUE
/backup: THRESHOLD_VALUE
</pre>

Replace <code>THRESHOLD_VALUE</code> with the threshold values as set in the INI file (do not add extra spaces; match the format exactly). 

Do not include any extra lines or information—only the two lines as described, in the exact order: first <code>/data1</code>, then <code>/backup</code>.

This summary file will be checked by an automated script for its exact content and format.
