Hey, I need your help analyzing a build artifact log on our CI server. We have a file at `/home/user/artifacts/build_log.txt` that records the name of every artifact produced during our nightly builds over the past month — one artifact name per line, with duplicates whenever the same artifact was built multiple times.

I need to generate a frequency report showing how many times each artifact was built, sorted from most-built to least-built. Please write the results to `/home/user/artifacts/artifact_freq.txt`.

The output file should contain exactly one line per artifact, formatted as:

```
<count> <artifact_name>
```

Where `<count>` is the number of times that artifact appears in the build log, and `<artifact_name>` is the artifact name exactly as it appears in the log. Lines must be sorted by count in **descending** order (highest count first). If two artifacts have the same count, they should be sorted **alphabetically** (ascending) by artifact name as a tiebreaker.

For example, if `libcore.so` was built 12 times and `libutils.so` was built 7 times, the file should start with:

```
12 libcore.so
7 libutils.so
```

There should be no leading spaces on any line — each line starts directly with the numeric count. No blank lines, no header, no trailing whitespace.

Once you've created `artifact_freq.txt`, also write a one-line summary to `/home/user/artifacts/summary.txt` in this exact format:

```
Total builds: <total_lines> | Unique artifacts: <unique_count> | Most built: <artifact_name> (<count> times)
```

Where `<total_lines>` is the total number of lines in `build_log.txt` (i.e., total artifact build events), `<unique_count>` is the number of distinct artifact names, and `<artifact_name>` and `<count>` correspond to the artifact with the highest build count (the first line of `artifact_freq.txt`).
