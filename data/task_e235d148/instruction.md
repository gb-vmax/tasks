I'm a mobile build engineer and I have a CI pipeline that generates Android build logs. I need a quick shell script to extract key build metrics from these logs and print a summary to stdout.

I have a build log file at `/home/user/pipeline/build.log`. I need you to write a shell script at `/home/user/pipeline/summarize_build.sh` that reads this log file and prints a formatted build summary.

The log file contains lines in these formats:
- Build start/end timestamps like: `[TIMESTAMP] BUILD STARTED: 2024-05-10 08:31:45` and `[TIMESTAMP] BUILD FINISHED: 2024-05-10 08:44:02`
- Module compile results like: `[INFO] Compiled module: auth SUCCESS` or `[INFO] Compiled module: payments FAILED`
- Warning lines like: `[WARN] Deprecated API usage in NetworkManager.kt`
- The overall build result like: `[RESULT] BUILD STATUS: SUCCESS` or `[RESULT] BUILD STATUS: FAILED`

The script must print EXACTLY the following format when run (values depend on what's in the log):

```
=== BUILD SUMMARY ===
Started:  <value from BUILD STARTED line>
Finished: <value from BUILD FINISHED line>
Status:   <value from BUILD STATUS line>
Modules compiled: <total number of Compiled module lines>
Modules failed:   <number of FAILED modules>
Warnings:         <number of [WARN] lines>
```

Requirements:
- The script must be executable (`chmod +x`).
- The script must read from `/home/user/pipeline/build.log` (hardcoded path is fine).
- Use only standard shell tools (`grep`, `awk`, `sed`, `wc`, etc.) — no Python, no Perl.
- The spacing/alignment in the output must match exactly: `Started:` and `Finished:` and `Status:` are followed by two spaces before the value; `Modules compiled:` is followed by one space; `Modules failed:` is followed by three spaces; `Warnings:` is followed by nine spaces. Look carefully at the format block above.

After writing the script, please also run it so I can confirm it works and produces the correct output for the existing log file.
