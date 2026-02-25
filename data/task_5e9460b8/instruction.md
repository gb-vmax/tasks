As a backup engineer, you need to verify the data integrity setting in the backup system configuration files. Check the values of the 'integrity_check' key in both the YAML file at /home/user/backup/settings.yaml and the TOML file at /home/user/backup/settings.toml. 

Create a log file at /home/user/backup/integrity_check_report.log. The log must be in the following format:

```
YAML integrity_check: <value>
TOML integrity_check: <value>
```

Replace &lt;value&gt; with the actual value for the 'integrity_check' key found in each file. The value should be shown exactly as it appears in each configuration file (e.g., 'true', 'false', 'yes', 'no'). Make sure the log file contains only these two lines, one for YAML and one for TOML in the specified order.
