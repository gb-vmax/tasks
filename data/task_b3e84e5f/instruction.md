I'm an infrastructure engineer and I need to quickly audit disk usage across a set of provisioned application directories before running an automated provisioning script. The directories have already been created at `/home/user/appdata`. I need you to generate a disk usage report at `/home/user/disk_report.txt` that I can feed into the provisioning pipeline.

The report must follow this exact format:

```
=== DISK USAGE REPORT ===
Generated: <hostname>

Top directories by size:
  <size_kb>K  <path>
  <size_kb>K  <path>
  <size_kb>K  <path>
  <size_kb>K  <path>
  <size_kb>K  <path>

Total usage: <total_kb>K
Available: <available_kb>K
```

Here are the exact requirements:

1. **Top directories by size**: List the 5 largest **immediate subdirectories** of `/home/user/appdata`, sorted by size in **descending** order (largest first). Each line must be indented with 2 spaces, followed by the size in kilobytes (as reported by `du -sk`), a tab character, and then the full absolute path of the directory. The format should look exactly like the output of `du -sk` but indented — for example: `  1024K  /home/user/appdata/logs`.

2. **Total usage**: The total disk usage of the entire `/home/user/appdata` directory, obtained with `du -sk /home/user/appdata`, expressed in kilobytes followed by `K`.

3. **Available**: The available space on the filesystem containing `/home/user/appdata`, as reported by `df -k` in the "Available" column for that mount point, expressed in kilobytes followed by `K`.

4. **Generated**: The hostname of the machine, as printed by the `hostname` command.

The report file must be written to `/home/user/disk_report.txt`. Every line must match the format above — spacing, indentation (2 spaces before size), and the `K` suffix are all checked by the automated test.

To be clear on the line format for each directory entry: it should be 2 spaces, then the numeric kilobyte value, then the letter `K`, then two spaces, then the absolute path. For example:
```
  512K  /home/user/appdata/cache
```

The "Total usage" and "Available" lines should follow the same `<number>K` format with no extra spaces.
