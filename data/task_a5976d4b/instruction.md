Hey, I'm doing a penetration test and I've got a file at `/home/user/pentest/scan_results.txt` that contains raw output from a vulnerability scanner. Each line of the file is the name of a vulnerability type that was detected (one vulnerability per line, some appear multiple times across different hosts). I need to quickly tally up how many times each vulnerability type appeared so I can prioritize my remediation report.

Can you process that file and write a frequency summary to `/home/user/pentest/vuln_summary.txt`?

The output file should list each vulnerability type and its count, sorted from most frequent to least frequent. Each line must follow this exact format:

```
<count> <vulnerability_name>
```

So for example, if "SSL_WEAK_CIPHER" appeared 5 times and "SMB_SIGNING_DISABLED" appeared 2 times, the output should be:

```
5 SSL_WEAK_CIPHER
2 SMB_SIGNING_DISABLED
```

There should be no leading spaces or extra whitespace — just the count, a single space, and then the vulnerability name. If two vulnerability types have the same count, they should be sorted alphabetically (A before Z) as a tiebreaker. The file should contain exactly one line per unique vulnerability type, with no blank lines and no header.
</think>
