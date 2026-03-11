Hey, I need your help processing a container registry log file. I'm trying to audit which microservices have images that are using deprecated base images so I can flag them for our team.

I have a tab-separated log file at `/home/user/registry/image_manifest.tsv`. Each line has the following fields (tab-separated):

```
<service_name>  <image_tag>  <base_image>  <pushed_by>  <size_mb>
```

I need you to do the following:

1. Extract all rows where the `base_image` field is either `ubuntu:18.04` or `debian:stretch` (these are our deprecated base images).

2. From those filtered rows, produce a report file at `/home/user/registry/deprecated_report.txt`. Each line in the report should have this exact format:

```
[DEPRECATED] <service_name> (<image_tag>) uses <base_image> — pushed by <pushed_by>
```

The lines should be sorted alphabetically by `service_name`.

3. Append a summary line at the very end of the report (after a blank line) in this exact format:

```
Total deprecated images: <count>
```

So the final file should look like:
```
[DEPRECATED] auth-service (v2.1.0) uses debian:stretch — pushed by alice
[DEPRECATED] user-service (v1.0.3) uses ubuntu:18.04 — pushed by bob
...

Total deprecated images: <N>
```

Please make sure the `—` character is an em dash (U+2014), not a regular hyphen. The spacing around it is ` — ` (space, em dash, space).

Can you create that report file for me?
