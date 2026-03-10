Hey, I'm an observability engineer and I need to quickly process a raw metrics export before updating our Grafana dashboard config. I have a file at `/home/user/metrics/service_latency.txt` that contains per-service latency data exported from our monitoring system.

The file has lines in this format:
```
service_name|environment|p50_ms|p95_ms|p99_ms
```

For example:
```
auth-service|production|12|45|120
```

I need you to do two things:

**Step 1:** Using `awk`, extract only the lines where `p99_ms` is greater than 100 (excluding the header line), and compute each service's "headroom ratio" defined as `p99_ms / p50_ms`, rounded to 1 decimal place. Write the results to `/home/user/metrics/high_latency.txt` in this exact format (tab-separated, no extra spaces):

```
SERVICE	ENV	P99	RATIO
<service_name>	<environment>	<p99_ms>	<ratio>
```

Sort the output lines (not the header) by `p99_ms` descending.

**Step 2:** Using `sed` on the file `/home/user/metrics/high_latency.txt` you just created, replace every occurrence of the environment name `production` with `prod` and `staging` with `stg`. Save the result **in place** (overwrite the same file).

The final `/home/user/metrics/high_latency.txt` should reflect both transformations.
