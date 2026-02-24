An IT support technician needs your help analyzing a ticket logging system. You are provided with the raw ticket titles file located at <code>/home/user/ticket_titles.txt</code>. Your task is to determine the frequency of each unique ticket title and list them in descending order of frequency.

Please:

1. Read the ticket titles from <code>/home/user/ticket_titles.txt</code>, which contains one ticket title per line (ticket titles are short phrases, may repeat, and are case-sensitive).
2. Count the number of times each unique title appears.
3. Create a report at <code>/home/user/ticket_frequency_report.txt</code> with the following format, where each line contains the count and the ticket title separated by a single space (count first), e.g. <code>3 Cannot connect to VPN</code>.
4. Sort the lines in the output file by count in descending numerical order. If two titles have the same count, order them lexicographically (case sensitive).

The output in <code>/home/user/ticket_frequency_report.txt</code> must match this exact format for the automated test to pass: <code>&lt;count&gt; &lt;ticket title&gt;</code> per line, sorted by count (most frequent first), then lexicographically.
