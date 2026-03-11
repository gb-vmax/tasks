Hey, I need help updating our CI/CD pipeline configuration. We have a GitLab CI YAML file at `/home/user/ci/pipeline.yml` that defines several jobs. The pipeline is currently using an outdated Docker image for the `build` job and the timeout is too low — I need you to fix both of those and then write a summary report.

Here's what I need done:

**1. Update the pipeline configuration at `/home/user/ci/pipeline.yml`:**

- Find the `build` job (it has a key `image:` under it) and change its image from `docker:20.10` to `docker:24.0`.
- Find the `build` job's `timeout:` field and change its value from `10 minutes` to `30 minutes`.
- Do NOT change anything else in the file — only those two values.

**2. Write a summary report to `/home/user/ci/pipeline_summary.txt`:**

After making the edits, read the updated pipeline file and produce a report with the **exact** following format (fill in the values from the updated file):

```
Pipeline Summary
================
Stages: <comma-separated list of stages in the order they appear in the `stages:` block>
Jobs: <comma-separated list of job names in the order they appear in the file>
Build image: <the image value from the build job>
Build timeout: <the timeout value from the build job>
```

Rules for the summary:
- The `Stages:` line should list the stage names joined by `, ` (comma + space), in the order they appear under the `stages:` key.
- The `Jobs:` line should list every top-level YAML key that is a job (i.e., not `stages`, not `image`, not `variables`, not `cache`, not `default`) joined by `, ` in the order they appear in the file. A job is any top-level key that has a `stage:` subkey.
- `Build image:` must be the exact string value of `image:` inside the `build` job after your edit.
- `Build timeout:` must be the exact string value of `timeout:` inside the `build` job after your edit.
- There should be no trailing spaces on any line and the file should end with a single newline character.
