Hey, I need your help with a quick FinOps task. I'm a cloud cost analyst and I need to update our cost alert configuration file and then generate a summary report line from it.

We have a cloud cost alert configuration file at `/home/user/finops/cost_alerts.cfg`. It's a simple key=value format file. I need you to do two things:

**Step 1: Update the configuration file**

In `/home/user/finops/cost_alerts.cfg`, find the following three keys and update their values:

- Change `monthly_budget_usd` from its current value to `12500`
- Change `alert_threshold_pct` from its current value to `80`
- Change `owner_email` from its current value to `finops-team@company.com`

All other lines in the file must remain exactly as they are (same order, same content).

**Step 2: Write a summary line**

After updating the config, create a new file at `/home/user/finops/budget_summary.txt` containing exactly one line in this format:

```
BUDGET: $<monthly_budget_usd> | ALERT AT: <alert_threshold_pct>% | CONTACT: <owner_email>
```

Using the updated values you just set. The file should contain exactly that one line and nothing else (no trailing newline after the line is fine, but the content must match exactly).

For example, with the values above it should read:
```
BUDGET: $12500 | ALERT AT: 80% | CONTACT: finops-team@company.com
```

Can you make both of those changes for me?
</think>
