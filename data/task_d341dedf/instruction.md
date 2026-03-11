I'm a container specialist managing a set of microservices and I need your help identifying memory pressure issues. I have a snapshot of container resource usage saved at `/home/user/containers/stats.txt`. This file was captured using `docker stats --no-stream` and has the following columns (space-separated, with a header line):

```
CONTAINER_ID   NAME              CPU%   MEM_USAGE/LIMIT         MEM%    NET_I/O        BLOCK_I/O
```

I need you to analyze this file and produce a memory optimization report at `/home/user/containers/report.txt`.

Here's exactly what the report must contain:

1. The name of the container using the **most memory** (by MEM% value).
2. Its memory usage and limit (copied exactly as it appears in the MEM_USAGE/LIMIT column, e.g. `512MiB / 1GiB`).
3. Its MEM% value.
4. A one-line recommendation based on the MEM% threshold:
   - If MEM% >= 80: `ACTION REQUIRED: Increase memory limit or scale horizontally.`
   - If MEM% >= 50: `WARNING: Monitor closely and consider increasing memory limit.`
   - If MEM% < 50: `OK: Memory usage is within acceptable range.`

The report must use this exact format (including spacing, colons, and newlines):

```
Container Memory Optimization Report
=====================================
Top memory consumer: <NAME>
Memory usage: <MEM_USAGE/LIMIT>
Memory percent: <MEM%>
Recommendation: <recommendation text>
```

There should be no trailing whitespace on any line and exactly one newline at the end of the file. The MEM% value in the report should be written exactly as it appears in the stats file (e.g., `73.45%`).
