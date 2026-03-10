Hey, I'm a network engineer and my monitoring server is running low on disk space. I suspect the network capture and log directory at `/home/user/net_data` is eating up space, but I need a quick summary to send to my team lead.

Can you help me analyze the disk usage of the subdirectories inside `/home/user/net_data` and write a sorted report to `/home/user/disk_report.txt`?

Here's exactly what I need in the report file:

1. The first line should be a header: `Disk Usage Report: /home/user/net_data`
2. Then a blank line.
3. Then the disk usage of each **direct subdirectory** of `/home/user/net_data`, one per line, in **descending order by size** (largest first). Each line must be in the format produced by `du -sh` — that is, a human-readable size (like `4.0K`, `12M`, `1.1G`) followed by a tab character, followed by the full path of the subdirectory.
4. Then a blank line.
5. Then a final line: `Total: <SIZE>` where `<SIZE>` is the total human-readable disk usage of the entire `/home/user/net_data` directory (as reported by `du -sh /home/user/net_data`).

For example, the file might look like this (your actual values will differ):

```
Disk Usage Report: /home/user/net_data

1.1G	/home/user/net_data/captures
240M	/home/user/net_data/logs
8.0K	/home/user/net_data/configs

Total: 1.4G
```

Please write the final output to `/home/user/disk_report.txt`.
