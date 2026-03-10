Hey, I'm a mobile build engineer and I need help analyzing our CI pipeline's build log. We had a full Android multi-module build run this morning, and the raw output is sitting at `/home/user/pipeline/build.log`. I need you to parse it and generate a structured summary report at `/home/user/pipeline/build_report.txt` that I can paste into our team's Slack channel.

Here's what the build log looks like: each line either reports a module's build result, a compiler warning, or a compiler error. The formats are:

- Build result lines: `[BUILD] module=<name> status=<SUCCESS|FAILED> duration_ms=<integer>`
- Warning lines: `[WARN] module=<name> file=<filename> message=<text>`
- Error lines: `[ERROR] module=<name> file=<filename> message=<text>`

I need you to parse `/home/user/pipeline/build.log` and produce `/home/user/pipeline/build_report.txt` with EXACTLY this format (no trailing spaces, use the exact section headers and separators shown):

```
=== ANDROID BUILD REPORT ===

-- Module Summary --
<module_name>: <status> (<duration_ms>ms)
<module_name>: <status> (<duration_ms>ms)
...

-- Build Statistics --
Total modules: <N>
Passed: <N>
Failed: <N>
Total build time: <N>ms
Slowest module: <module_name> (<duration_ms>ms)
Fastest module: <module_name> (<duration_ms>ms)

-- Warnings by Module --
<module_name>: <count> warning(s)
<module_name>: <count> warning(s)
...

-- Errors by Module --
<module_name>: <count> error(s)
<module_name>: <count> error(s)
...

-- Action Items --
FAILED modules: <module1>, <module2>, ...
Total warnings: <N>
Total errors: <N>
```

Specific formatting rules:
- In the "Module Summary" section, list modules in the order they appear in the log file. Each line is `<module_name>: <status> (<duration_ms>ms)`.
- In "Build Statistics", "Total build time" is the sum of all `duration_ms` values. "Slowest module" and "Fastest module" are determined by `duration_ms`.
- In "Warnings by Module", list only modules that have at least one warning, sorted by warning count descending. If two modules have the same count, sort them alphabetically.
- In "Errors by Module", list only modules that have at least one error, sorted by error count descending. If two modules have the same count, sort them alphabetically.
- In "Action Items", "FAILED modules" lists only modules whose status is FAILED, in the order they appear in the log file, separated by `, `. If no modules failed, write `FAILED modules: none`.
- If there are no warnings at all, the "Warnings by Module" section should contain a single line: `(none)`. Same for errors.
- There is exactly one blank line between sections (after the section header line and before the next `--` header).

The log file is already at `/home/user/pipeline/build.log`. Please parse it and write the report to `/home/user/pipeline/build_report.txt`.
