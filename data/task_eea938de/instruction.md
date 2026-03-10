I'm an IT support manager and I need to analyze our helpdesk ticket log from last month to generate a summary report for our team meeting. The ticket data is stored in `/home/user/support/tickets.tsv` as a tab-separated file with a header row followed by ticket entries.

The file has these columns (in order): `ticket_id`, `date`, `category`, `technician`, `status`, `error_code`, `priority`

I need you to analyze the ticket data and produce a report at `/home/user/support/summary_report.txt`. The analysis involves several independent frequency counts that need to be combined into one file.

Here's the exact format I need — please match this precisely, including spacing, capitalization, and the separators:

```
=== IT SUPPORT TICKET SUMMARY ===

--- Tickets by Category ---
<count> <category>
<count> <category>
...

--- Tickets by Technician ---
<count> <technician>
<count> <technician>
...

--- Tickets by Status ---
<count> <status>
<count> <status>
...

--- Top Error Codes ---
<count> <error_code>
<count> <error_code>
...

--- Tickets by Priority ---
<count> <priority>
<count> <priority>
...
```

Rules for each section:

1. **Tickets by Category**: Count how many tickets belong to each category. Sort by count descending. If two categories have the same count, sort alphabetically ascending by category name.

2. **Tickets by Technician**: Count how many tickets each technician handled. Sort by count descending. Ties broken alphabetically ascending by technician name.

3. **Tickets by Status**: Count how many tickets have each status. Sort by count descending. Ties broken alphabetically ascending.

4. **Top Error Codes**: Count occurrences of each error code. Sort by count descending. Only include the TOP 5 error codes (by count). If there are ties at position 5, include all tied entries (so you might have more than 5 lines). Ties broken alphabetically ascending.

5. **Tickets by Priority**: Count tickets for each priority level. Sort by count descending. Ties broken alphabetically ascending.

The counts are separated from the labels by a single space. Do not include the header row in any counts. Do not include blank lines within any section (only the blank lines shown in the format template above, between sections). The report ends with a newline after the last line of the last section (no trailing blank line).

After generating the report, also create `/home/user/support/technician_load.txt` — a plain list of technician names, one per line, in order from most tickets to fewest, with ties broken alphabetically. This file should contain ONLY the technician names (no counts), one per line, with a final newline.

Can you run this analysis and generate both output files?
