Hey, I need your help with a quick environment configuration cleanup for our cloud cost optimization project. We have a dotenv file at `/home/user/finops/.env` that contains a mix of settings — some AWS credentials, some cost alert thresholds, and some stale/unused variables. I need you to clean it up and update a few values.

Here's what I need done:

**Step 1: Update specific variable values in place**

In `/home/user/finops/.env`, update the following variables to their new values:
- `COST_ALERT_THRESHOLD_USD` should be changed to `750`
- `MONTHLY_BUDGET_USD` should be changed to `5000`
- `ALERT_EMAIL` should be changed to `finops-team@company.com`

**Step 2: Remove stale variables**

Remove the following variables entirely from the file (delete the entire line):
- `UNUSED_LEGACY_KEY`
- `OLD_REGION_OVERRIDE`
- `DEBUG_VERBOSE`

**Step 3: Write a sanitized export file**

Create a new file at `/home/user/finops/.env.production` that contains ONLY the non-secret variables (i.e., exclude any line where the key contains `KEY`, `SECRET`, or `TOKEN`). The variables to include should be written in the exact same `KEY=VALUE` format (no `export` prefix, no quotes added). The file should preserve the same order as the variables appear in `.env` after your edits. Do not include blank lines or comment lines in `.env.production`.

The final `/home/user/finops/.env.production` should look exactly like this (the lines and values must match precisely):

```
AWS_REGION=us-east-1
COST_ALERT_THRESHOLD_USD=750
MONTHLY_BUDGET_USD=5000
ALERT_EMAIL=finops-team@company.com
ENABLE_COST_EXPLORER=true
REPORT_INTERVAL_DAYS=7
COST_ALLOCATION_TAG=CostCenter
```

Make sure the updated `/home/user/finops/.env` retains all the other variables (credentials and remaining config) with the stale ones removed and the three values updated. The `.env` file must not contain `UNUSED_LEGACY_KEY`, `OLD_REGION_OVERRIDE`, or `DEBUG_VERBOSE` anywhere.
