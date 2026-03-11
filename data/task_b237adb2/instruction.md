Hey, I need your help with a support ticket. One of our developers submitted a ticket saying that the staging environment configuration file is pointing to the wrong database host and has an outdated API key. I need you to fix the `.env` file for the staging app and then verify the corrected values are exported correctly into a summary file.

Here's what needs to happen:

The staging environment file is located at `/home/user/apps/staging/.env`. It currently has some incorrect values that are causing connection failures. The ticket says:

1. `DB_HOST` needs to be changed to `db-staging.internal.company.com`
2. `API_KEY` needs to be changed to `sk-staging-9f2a1c4e8b3d7f6a`

The other variables in the file must remain **exactly as they are** — do not add, remove, or reorder any lines.

After updating the `.env` file, I need you to produce a verification summary at `/home/user/apps/staging/env_summary.txt`. This file should list only the following four variables in this exact order and format (one per line, no spaces around the `=`):

```
DB_HOST=db-staging.internal.company.com
DB_PORT=5432
API_KEY=sk-staging-9f2a1c4e8b3d7f6a
APP_ENV=staging
```

The summary file should contain exactly those 4 lines, in that exact order, with no trailing spaces, no blank lines, and a newline at the end of the last line.
