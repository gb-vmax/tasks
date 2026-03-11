Hey, I need your help analyzing a configuration change log from our deployment system. The log file is at `/home/user/config_changes.log` and it records every configuration change made by our team.

Each line in the log follows this format:
```
[TIMESTAMP] USER=<username> COMPONENT=<component> ACTION=<action> STATUS=<status>
```

For example:
```
[2024-06-10 08:14:02] USER=alice COMPONENT=database ACTION=update STATUS=success
[2024-06-10 09:30:55] USER=bob COMPONENT=network ACTION=rollback STATUS=failure
```

I need you to generate a summary report saved to `/home/user/config_report.txt`. The report should contain exactly the following sections, filled in with the correct values from the log:

```
CONFIG CHANGE REPORT
====================
Total changes: <N>
Successful changes: <N>
Failed changes: <N>

Changes by user:
  alice: <N>
  bob: <N>
  carol: <N>

Changes by component:
  database: <N>
  firewall: <N>
  network: <N>
  webserver: <N>
```

A few important formatting notes:
- The users in the "Changes by user" section must be listed in alphabetical order, one per line, with exactly two leading spaces before the name.
- The components in the "Changes by component" section must also be in alphabetical order, one per line, with exactly two leading spaces before the name.
- Only include users and components that actually appear in the log file.
- There is no trailing newline after the last component line.
- The counts after the colon should have exactly one space before the number.

Please generate this report from the existing log file.
