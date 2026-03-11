I'm an infrastructure engineer and I have an old server provisioning script sitting at `/home/user/provisioning/provision.sh` that a former colleague wrote. I need to run it to set up a test environment and capture its output into a structured report.

Here's what I need you to do:

1. The script at `/home/user/provisioning/provision.sh` takes a single argument: the path to a config file. Run it using the config file at `/home/user/provisioning/env.conf`. The script may not be executable yet — make sure it can run.

2. The script will print output to stdout. Capture that output and write it to `/home/user/provisioning/run.log`.

3. After capturing the output, create a final report file at `/home/user/provisioning/report.txt` with the following exact format:

```
=== PROVISIONING REPORT ===
Config: /home/user/provisioning/env.conf
Exit code: 0
Lines logged: <N>
Services provisioned: <M>

--- LOG ---
<full contents of run.log here>
```

Where:
- `<N>` is the number of lines in `run.log` (the raw stdout from the script).
- `<M>` is the count of lines in `run.log` that begin with the prefix `[DONE]` (these lines indicate a successfully provisioned service).
- The `--- LOG ---` section must be followed by a newline and then the exact verbatim contents of `run.log`, with no trailing newline added beyond what the script itself produced.
- `Exit code:` should reflect the actual exit code of the provisioning script.

Do not modify `provision.sh` or `env.conf`. The report file should be created purely from the script's output.
