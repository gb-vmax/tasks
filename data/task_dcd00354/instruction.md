I'm a build engineer and I need your help analyzing a CI build log to identify which artifacts failed to package. We had a nightly build run and some artifacts failed. The build log is at `/home/user/builds/nightly.log`.

Each line in the log follows this format:
```
[TIMESTAMP] [STATUS] artifact=<name> size=<bytes>
```

For example:
```
[2024-11-01 02:13:45] [SUCCESS] artifact=libcore-2.1.0.tar.gz size=104857
[2024-11-01 02:14:02] [FAILED] artifact=libui-3.0.1.tar.gz size=0
```

I need you to extract every artifact that has a `[FAILED]` status and write just the artifact names (nothing else — no timestamps, no sizes, no brackets, no "artifact=" prefix) to a new file at `/home/user/builds/failed_artifacts.txt`, one artifact name per line, in the same order they appear in the log.

The file should contain only the artifact names and a trailing newline at the end. No blank lines, no extra whitespace.

Can you do that for me?
