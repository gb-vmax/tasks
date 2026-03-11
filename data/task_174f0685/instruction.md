Hey, I need your help setting up some symlinks for our FinOps reporting workflow. Here's the situation:

We have monthly cloud cost reports stored in versioned directories under `/home/user/finops/reports/`. Right now the latest reports for AWS, GCP, and Azure are sitting in their respective month folders, but our downstream cost-analysis scripts are hardcoded to read from a `current/` directory that should always point to the latest data. Instead of copying files around every month, we want to use symbolic links so the `current/` directory always reflects the newest reports without duplicating data.

Here's what I need you to do:

1. The directory `/home/user/finops/reports/current/` already exists (it's empty). Inside that directory, create three symbolic links — one for each cloud provider — pointing to the actual report files located elsewhere under `/home/user/finops/reports/`:

   - Create a symlink named `aws.csv` inside `/home/user/finops/reports/current/` that points to `/home/user/finops/reports/2024-06/aws_costs_2024-06.csv`
   - Create a symlink named `gcp.csv` inside `/home/user/finops/reports/current/` that points to `/home/user/finops/reports/2024-06/gcp_costs_2024-06.csv`
   - Create a symlink named `azure.csv` inside `/home/user/finops/reports/current/` that points to `/home/user/finops/reports/2024-06/azure_costs_2024-06.csv`

2. After creating the symlinks, produce a summary file at `/home/user/finops/reports/current/links_summary.txt`. The file must contain exactly three lines, one per symlink, in alphabetical order by provider name, in this format:

```
aws.csv -> /home/user/finops/reports/2024-06/aws_costs_2024-06.csv
azure.csv -> /home/user/finops/reports/2024-06/azure_costs_2024-06.csv
gcp.csv -> /home/user/finops/reports/2024-06/gcp_costs_2024-06.csv
```

Each line must be exactly `<link_name> -> <absolute_target_path>` with a single space on each side of the `->` arrow. No trailing spaces, no blank lines.

The symlinks themselves must be real symbolic links (not copies of the files), and they must resolve correctly — meaning reading through the symlink should return the actual content of the target CSV file.

Can you set this up for me?
