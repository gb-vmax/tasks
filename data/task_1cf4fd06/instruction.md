Hey, I need your help benchmarking a data processing script that runs in our CI/CD pipeline. We've been seeing slow build times and I want to get baseline performance numbers before we start optimizing. The script is at `/home/user/pipeline/process.sh`.

I want you to run the script **10 times** using the `time` command (via a loop), capture the real elapsed time for each run, and then compute statistics and write them to a report.

Here's exactly what I need done:

**Step 1: Run the benchmark**

Run `/home/user/pipeline/process.sh` 10 times, measuring the real elapsed wall-clock time of each run using bash's built-in `time`. Collect the elapsed seconds (as a decimal number, e.g. `0.043`) for each of the 10 runs.

**Step 2: Compute statistics**

From the 10 timing samples, compute:
- **min**: the smallest value
- **max**: the largest value
- **avg**: the arithmetic mean

All values must be rounded/formatted to **3 decimal places**.

**Step 3: Write the report**

Write the results to `/home/user/pipeline/benchmark_report.txt` with this **exact** format (including spacing and punctuation):

```
benchmark: process.sh
runs: 10
min: <X.XXX>s
max: <X.XXX>s
avg: <X.XXX>s
```

Where `<X.XXX>` is each computed value with exactly 3 decimal places followed immediately by `s` (no space between the number and `s`).

For example, a valid file might look like:
```
benchmark: process.sh
runs: 10
min: 0.031s
max: 0.057s
avg: 0.041s
```

**Requirements:**
- The file at `/home/user/pipeline/benchmark_report.txt` must exist after you're done.
- The format must match exactly — no extra blank lines, no trailing spaces, exactly 5 lines total.
- The values must be derived from actually running the script 10 times (not hardcoded).
- Do not modify `/home/user/pipeline/process.sh`.
