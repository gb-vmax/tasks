Hey, I need your help reorganizing a ticket export file so I can import it into our new helpdesk system. The file is at `/home/user/tickets/open_tickets.tsv` — it's a tab-separated file that our old system exported, but the new system requires the columns in a completely different order, and it also wants us to drop a couple of columns it doesn't need.

Here's the situation: the current file has these columns in this order:
1. `ticket_id`
2. `assigned_agent`
3. `priority`
4. `created_date`
5. `category`
6. `status`
7. `customer_email`

The new helpdesk system requires the file to have only these columns, in exactly this order:
1. `ticket_id`
2. `customer_email`
3. `priority`
4. `category`
5. `assigned_agent`

So you need to drop `created_date` and `status` entirely, and reorder the remaining five columns as shown above.

Please produce the reformatted file at `/home/user/tickets/import_ready.tsv`. It must be tab-separated, include the header row as the first line, and contain all the data rows from the original file (just reordered/trimmed).

The output file should have the header line:
```
ticket_id	customer_email	priority	category	assigned_agent
```
followed by one data row per ticket, all tab-separated, in the same row order as the original file.
