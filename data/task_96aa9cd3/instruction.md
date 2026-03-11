I'm an operations engineer and I need help triaging a set of incidents from our on-call log. We have a raw incident log at `/home/user/oncall/incidents.log`. Each line has this pipe-delimited format:

```
<timestamp>|<incident_id>|<severity>|<service>|<message>
```

I need you to process this file and produce a triage summary at `/home/user/oncall/triage_summary.txt`.

Here's exactly what I need:

**Step 1:** Extract only the lines where severity is `CRITICAL` or `HIGH` (the third field). Ignore `LOW` and `MEDIUM` lines entirely.

**Step 2:** From those filtered lines, use `awk` to reformat each line into this format:

```
[<severity>] <incident_id> | <service>: <message>
```

For example, a raw line like:
```
2024-06-01T08:15:00|INC-0042|CRITICAL|auth-service|Token validation failure
```
should become:
```
[CRITICAL] INC-0042 | auth-service: Token validation failure
```

**Step 3:** Use `sed` to make two substitutions on the reformatted lines:
- Replace the word `failure` (case-insensitive) with `FAILURE` everywhere it appears in the message text.
- Replace the word `timeout` (case-insensitive) with `TIMEOUT` everywhere it appears in the message text.

**Step 4:** Write the final processed lines to `/home/user/oncall/triage_summary.txt`. The lines should appear in the same order they appear in the original file. There should be no blank lines in the output file, and no trailing whitespace on any line.
