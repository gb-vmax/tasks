You are working as a deployment engineer preparing to roll out a critical service update. In the directory <code>/home/user/app-deployment</code>, you have three files:
<code>/home/user/app-deployment/server-list.txt</code> (listing server hostnames),
<code>/home/user/app-deployment/version-info.txt</code> (containing the service version for each server), and
<code>/home/user/app-deployment/deployment.log</code> (an initial log file which may or may not already exist).

Your tasks are as follows:

1. **Using <code>awk</code>:**  
   - For each hostname in <code>server-list.txt</code>, find the corresponding version in <code>version-info.txt</code> and create a report file at <code>/home/user/app-deployment/host-version-report.csv</code>.  
   - The <code>host-version-report.csv</code> must be a comma-separated values file (CSV) with the columns: Hostname,Version.  
   - The first line in the file must be the header (<code>Hostname,Version</code>), followed by one line for each hostname in <code>server-list.txt</code>.  
   - Each hostname listed must appear only once, in the same order as in <code>server-list.txt</code>.  
   - If a hostname in <code>server-list.txt</code> has no corresponding entry in <code>version-info.txt</code>, set its Version to <code>UNKNOWN</code>.

2. **Using <code>sed</code>:**  
   - Update <code>deployment.log</code> so every line containing the phrase <code>DEPLOY START</code> is replaced with the phrase <code>DEPLOY INITIATED</code>.  
   - Do not modify any other content, empty lines, or lines not containing that exact phrase.  
   - Overwrite <code>deployment.log</code> in-place.

3. **Finally,** output to the console the total number of lines in the updated <code>deployment.log</code> which contain the word <code>FAILED</code> (case-sensitive substring match), and also append a summary line to <code>/home/user/app-deployment/host-version-report.csv</code>:
   - The summary line should be:  
     <code>TOTAL_FAILED,[number]</code>  
     Replace <code>[number]</code> with the count of lines containing <code>FAILED</code> in the final <code>deployment.log</code>.

Make sure the permissions remain as readable and writable by the current user for all files you modify or create.

**File formats:**

- <code>server-list.txt</code>: each hostname per line, no header.
- <code>version-info.txt</code>: each line is <code>hostname version</code>, space-separated, multiple hostnames possible, no header.
- <code>host-version-report.csv</code>: follows the required CSV format detailed above, with header, one line per hostname, and the summary line at the end.
- <code>deployment.log</code>: plain text log file, may contain any lines.

The automated test will verify the precise format of <code>host-version-report.csv</code>, the in-place changes in <code>deployment.log</code>, and the correct number output and summary line.
