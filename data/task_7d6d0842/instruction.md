As a backup engineer, you need to verify and log the location configuration for periodic data integrity checks. There are two configuration files: the first is a YAML file located at <code>/home/user/configs/backup.yml</code>, and the second is a TOML file at <code>/home/user/configs/backup.toml</code>. 

In <code>backup.yml</code>, there is a key named <code>integrity_check_dir</code> (which specifies the directory used for integrity checks). In <code>backup.toml</code>, the equivalent configuration is under <code>[checks]</code> as <code>integrity_check_dir</code>.

Your task is to extract the value of <code>integrity_check_dir</code> from both files and write a log file at <code>/home/user/backup_integrity_locations.log</code> in the following format:

<pre>
[backup.yml]
integrity_check_dir: &lt;value from backup.yml&gt;

[backup.toml]
integrity_check_dir: &lt;value from backup.toml&gt;
</pre>

For example, if <code>integrity_check_dir</code> is <code>/mnt/storage/integrity</code> in both files, the log should appear as:

<pre>
[backup.yml]
integrity_check_dir: /mnt/storage/integrity

[backup.toml]
integrity_check_dir: /mnt/storage/integrity
</pre>

Please ensure the log file is created exactly as shown above, including blank lines between sections.
