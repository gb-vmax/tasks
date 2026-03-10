I'm a storage administrator and I need your help processing a disk usage report. I have a file at `/home/user/disk_report.txt` that contains output in a `df`-like format. I need to extract the over-capacity filesystems and reformat the data into a clean summary file.

The file `/home/user/disk_report.txt` contains lines in this format (whitespace-separated columns):

```
Filesystem         Size  Used  Avail  Use%  Mounted_on
```

For example:
```
/dev/sda1          500G  120G  380G   24%   /
```

**Your task:**

Process `/home/user/disk_report.txt` and create a new file at `/home/user/alerts.txt` that contains only the filesystems where the usage percentage is **80% or greater**. The header line (starting with `Filesystem`) must be skipped and must not appear in the output.

Each line in `alerts.txt` must follow this exact format:

```
ALERT: <Mounted_on> is at <Use%> capacity (<Used> used of <Size>)
```

For example, if a filesystem has Size=500G, Used=450G, Use%=90%, and Mounted_on=/data, the output line would be:

```
ALERT: /data is at 90% capacity (450G used of 500G)
```

The lines in `alerts.txt` must appear in the same order as they appear in the input file. Do not include any trailing blank lines. The `Use%` value in the output must include the `%` sign exactly as it appears in the input (e.g., `85%`, `100%`).

Please process the file and write the result to `/home/user/alerts.txt`.
