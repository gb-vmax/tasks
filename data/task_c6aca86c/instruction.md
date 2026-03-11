Hey, I need some quick help analyzing a CI/CD pipeline timing report. Our pipelines have been running slower than expected lately and my manager asked me to identify the bottleneck in our main build pipeline.

I have a pipeline timing log at `/home/user/ci/pipeline_timings.log`. Each line in this file represents one stage of the pipeline and follows this exact format:

```
<stage_name> <duration_seconds>
```

For example:
```
checkout 12
unit_tests 94
```

I need you to do two things:

**1.** Find the stage with the highest `duration_seconds` value in the file and write a one-line summary to `/home/user/ci/bottleneck.txt` in this exact format:

```
bottleneck: <stage_name> (<duration_seconds>s)
```

For example, if `unit_tests` took the longest at 94 seconds, the file should contain:
```
bottleneck: unit_tests (94s)
```

There should be no trailing newline issues — just a single line in the file. The parentheses, the `s` suffix, and the colon-space after `bottleneck` must all be present exactly as shown.

**2.** Append a second line to `/home/user/ci/bottleneck.txt` with the total pipeline duration (the sum of all stage durations), in this exact format:

```
total_duration: <sum>s
```

So the final file `/home/user/ci/bottleneck.txt` should contain exactly two lines — the bottleneck line first, then the total duration line.

Please help me figure this out so I can report the pipeline bottleneck to the team.
