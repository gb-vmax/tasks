I'm an incident responder and I've been handed a legacy Python script that was supposedly working fine last month but is now throwing errors. The script is at `/home/user/incident/analyze_log.py` and it's supposed to parse a server log file at `/home/user/incident/server.log` and print a summary to stdout.

I need you to do the following:

1. Run the script as-is (`python3 /home/user/incident/analyze_log.py`) and capture its stderr output to a file at `/home/user/incident/error.txt`. Stdout should still appear on the terminal (or be discarded — I only need the stderr captured). The script will fail — that's expected.

2. Read the error output to understand what's wrong. The script is failing because it expects an environment variable called `LOG_THRESHOLD` to be set (it tries to read it with `os.environ["LOG_THRESHOLD"]` and crashes with a `KeyError` if it's missing). Set this environment variable to the value `3` and re-run the script. This time, it should succeed.

3. When the script runs successfully, it will print its output to stdout. Capture that successful output to a file at `/home/user/incident/summary.txt`.

The final file `/home/user/incident/summary.txt` should contain exactly:

```
Lines above threshold: 4
Flagged entries:
  [ERROR] disk quota exceeded
  [ERROR] connection timeout
  [ERROR] failed to write to socket
  [ERROR] null pointer in handler
```

And `/home/user/incident/error.txt` should contain exactly:

```
Traceback (most recent call last):
  File "/home/user/incident/analyze_log.py", line 10, in <module>
    threshold = int(os.environ["LOG_THRESHOLD"])
KeyError: 'LOG_THRESHOLD'
```

Can you run the script, capture the error, fix the environment variable issue, and save the successful output?
