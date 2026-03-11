I'm a security engineer and I need your help analyzing an authentication log before rotating API credentials. We've had some suspicious activity and I want to know which API keys are being used most frequently, so I can prioritize which ones to rotate first.

There's an authentication log file at `/home/user/security/auth.log`. Each line contains a timestamp, a result (SUCCESS or FAILED), and an API key identifier, separated by spaces, like this:

```
2024-05-01T08:00:01Z SUCCESS key_alpha
2024-05-01T08:00:05Z FAILED  key_beta
...
```

I need you to extract just the API key identifiers from this file, count how many times each one appears (regardless of success or failure), and write a frequency report to `/home/user/security/key_frequency.txt`.

The output file must have exactly one line per unique API key, in this format:

```
<count> <key_name>
```

The lines must be sorted by count in **descending** order (most-used key first). If two keys have the same count, they should appear in **reverse alphabetical** order (e.g., `key_zeta` before `key_alpha`).

There should be no leading spaces on any line, and no blank lines in the file.

For example, if `key_gamma` appears 7 times and `key_beta` appears 3 times, the file should start with:

```
7 key_gamma
3 key_beta
```

Please create the `/home/user/security/key_frequency.txt` file with these exact contents based on the log data.
</think>
