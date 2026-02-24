As a release manager, you are preparing for new deployments. In the directory <code>/home/user/releases</code>, there is a file named <code>pending_deployments.csv</code>. This CSV file contains upcoming deployment records, each on a new line, with the following comma-separated columns (no header): 

<pre>
release_id,application,version,scheduled_date,approved
</pre>

For example:
<pre>
1042,Inventory,2.3.5,2024-07-01,no
1043,Checkout,1.4.1,2024-07-02,yes
1044,Warehouse,1.2.9,2024-07-05,no
</pre>

You need to produce a new text file at <code>/home/user/releases/deployments_ready.txt</code> containing only the records where the <code>approved</code> column value is "yes". Each approved deployment should be output as a single line in the following format (without any separators or extra text before/after):

<pre>
RELEASE {release_id}: {application} v{version} scheduled for {scheduled_date}
</pre>

For example, the sample above would result in:
<pre>
RELEASE 1043: Checkout v1.4.1 scheduled for 2024-07-02
</pre>

Ensure the output file only contains the approved deployments, with one per line, regardless of order. Do not include a header or any other information.
