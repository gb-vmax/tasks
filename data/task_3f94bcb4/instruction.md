You are a platform engineer maintaining CI/CD pipelines. In the directory /home/user/build_logs, you have a log file named pipeline.log, which contains textual output from a recent CI/CD pipeline run. Your task is as follows:

1. Extract and list all lines from /home/user/build_logs/pipeline.log that contain the word "ERROR" (case-sensitive).
2. Save these lines into a new file located at /home/user/build_logs/pipeline_errors.txt.
3. The resulting /home/user/build_logs/pipeline_errors.txt file should contain only the extracted lines, in their original order, and no additional lines or text.

For verification, please create a summary file at /home/user/build_logs/extraction_summary.txt with the exact following format:

```
Total ERROR lines extracted: <number>
First ERROR line: <the exact content of the first ERROR line, or "NONE" if no ERROR line exists>
```

Replace &lt;number&gt; with the count of lines containing "ERROR" and &lt;the exact content of the first ERROR line&gt; with the first such line found in pipeline.log. If no ERROR lines are present, pipeline_errors.txt should be an empty file, and the string "NONE" should appear as the value for the first ERROR line in extraction_summary.txt.
