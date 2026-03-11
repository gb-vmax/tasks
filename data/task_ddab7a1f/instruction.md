I'm a FinOps analyst and I need your help cleaning up our cloud cost reporting directory. We've accumulated a bunch of stale daily cost report files that are no longer needed for active analysis — specifically any files under `/home/user/cost_reports` that are named with the pattern `daily_*.csv` and are larger than 10 kilobytes.

I need you to do two things:

**Step 1:** Use `find` and `xargs` to compute the total size (in bytes) of all `daily_*.csv` files under `/home/user/cost_reports` that are **larger than 10 kilobytes** (i.e., strictly greater than 10KB, meaning `find`'s `-size +10k` flag). Write only the total byte count as a single integer on its own line to `/home/user/cost_reports/savings_report.txt`. The byte count must come from running `wc -c` on those files via xargs and extracting the grand total line — the final number that `wc -c` prints on the "total" line when given multiple files.

For example, if the matching files total 45678 bytes, the file should contain exactly:
```
45678
```

**Step 2:** Use `find` and `xargs` to **delete** all those same `daily_*.csv` files that are larger than 10 kilobytes. After deletion, none of those oversized daily CSV files should remain anywhere under `/home/user/cost_reports`. Any `daily_*.csv` files that are 10KB or smaller must be left untouched, and any files with different names (including `savings_report.txt` and any `monthly_*.csv` files) must also remain untouched.

Please make sure `savings_report.txt` is written before the large files are deleted.
