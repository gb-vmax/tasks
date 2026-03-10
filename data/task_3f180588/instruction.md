Hey, I need your help with a quick cloud cost analysis. I'm a FinOps analyst and I have a log of all cloud resource charges for the month at `/home/user/finops/charges.csv`. Each line is a comma-separated record in this format:

```
resource_id,service_type,region,team,cost_usd
```

For example:
```
r-0a1b2c,EC2,us-east-1,platform,142.50
r-0d4e5f,S3,eu-west-1,data,18.00
```

I need to figure out which teams are spinning up the most individual resource charges (i.e., how many line items — not total dollar cost — are billed to each team). This helps us flag teams that might be over-provisioning.

Please produce a report at `/home/user/finops/team_charge_counts.txt` that lists each team name alongside the number of charge line items attributed to them, sorted from highest to lowest count. If two teams have the same count, sort them alphabetically by team name.

The output file should have one line per team in exactly this format:
```
<count> <team>
```

For example:
```
14 platform
9 data
9 analytics
3 infra
```

Note the single space between the count and the team name, and no header line — just the data rows. No trailing spaces.
