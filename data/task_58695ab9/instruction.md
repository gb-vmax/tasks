Hey, I need some help analyzing build failure logs from our mobile CI pipeline. I've got a file at `/home/user/pipeline/build_failures.log` that contains one failure reason per line — these get appended every time a build fails across our Android and iOS pipelines throughout the day.

I need to quickly see which failure types are hitting us the most so I can prioritize what to fix first. Can you process that file and generate a frequency report at `/home/user/pipeline/failure_report.txt`?

The report should list each unique failure reason along with how many times it occurred, sorted from most frequent to least frequent. The exact format for each line should be:

```
<count> <failure reason>
```

Where `<count>` and `<failure reason>` are separated by a single space, and `<count>` is just the plain number with no leading spaces or zero-padding. If two failure reasons have the same count, sort them alphabetically (ascending) by the failure reason text.

For example, if "Gradle sync failed" appeared 5 times and "Code signing error" appeared 3 times, the first two lines of the report would be:
```
5 Gradle sync failed
3 Code signing error
```

The output file should contain exactly one line per unique failure reason, with no blank lines, no header, and no trailing whitespace.

The source file is already at `/home/user/pipeline/build_failures.log` — please process it and write the result to `/home/user/pipeline/failure_report.txt`.
</think>
