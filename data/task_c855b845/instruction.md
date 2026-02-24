You are acting as a DevOps engineer tasked with diagnosing issues on a development system that uses `apt` for package management. There are two main troubleshooting steps:

1. **List all currently installed packages and export the list to a file** located at `/home/user/devops/logs/installed_packages.txt`. The log file must contain one package name per line, sorted alphabetically in ascending order, and should not include any headers or additional metadata; only the package names should be present.

2. **Check for any partially installed or broken packages** and record the findings in `/home/user/devops/logs/package_issues.log`. This file must be created. If broken or partially installed packages exist, list each problematic package on a new line in the format:
   ```
   [BROKEN] <package-name>
   ```
   If there are no issues found, the file should contain only:
   ```
   No broken packages found.
   ```

Additionally:

- Both log files must be present upon completion.
- The `/home/user/devops/logs/` directory must exist and be writable by `user`.
- If any commands produce output to the terminal as part of the investigation, that is acceptable; however, automated verification will only inspect the exact contents of the above log files.
