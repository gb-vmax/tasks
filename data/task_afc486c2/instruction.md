You are a build engineer and need to design a simple data artifact pipeline with basic error recovery. Perform the following:

1. In your home directory (/home/user), there are two files provided:
   - /home/user/artifacts/build-output.txt (contains build artifact data in a single-line CSV format: `artifact_id,build_time,status`)
   - /home/user/artifacts/failed-artifacts.txt (any missing or failed artifact IDs will be appended here as single lines, one artifact_id per line)

2. Your task:
   a. Read the artifact IDs from /home/user/artifacts/build-output.txt. Each line will be in the CSV format: e.g. `artifact42,2024-06-12T16:12:03Z,SUCCESS`.
   b. Extract only the artifact_id of those entries whose `status` field is not "SUCCESS". For each, append its artifact_id to /home/user/artifacts/failed-artifacts.txt, one per line, with no extra whitespace.
   c. Create an artifact report log file at /home/user/artifacts/artifact-pipeline.log listing actions performed:
      - For every artifact in build-output.txt whose status is not "SUCCESS", write a line: `RECOVERED: [artifact_id]`
      - For every artifact with status "SUCCESS", write a line: `PROCESSED: [artifact_id]`
   d. Format for /home/user/artifacts/artifact-pipeline.log:
      - Each line should use the labels above and have the artifact_id in square brackets as demonstrated.
      - No blank lines, one log entry per artifact, in the order they appear in build-output.txt.

3. If any artifact_id is added to failed-artifacts.txt during the process, output to the console: `One or more artifacts failed and are recorded.`

The format of /home/user/artifacts/artifact-pipeline.log will be checked. The process should append to failed-artifacts.txt if new failures are identified. Console output is expected only when a failure is appended.
