A configuration manager wants to quickly spot any changes made to a system configuration file. You have been provided with a file named <code>/home/user/original.conf</code> containing system settings, and a newer version named <code>/home/user/updated.conf</code>. Generate a changelog file named <code>/home/user/change.log</code> that lists ONLY the lines that are present in <code>/home/user/updated.conf</code> but missing from <code>/home/user/original.conf</code> (i.e., the added lines). 

The log format must be as follows: each newly added line must be written exactly as it appears in <code>/home/user/updated.conf</code>, prefixed by "<code>ADDED:</code> " (including the space after the colon). Do not include any lines that are present in both files, and do not include deleted or modified lines. The order of the added lines in <code>/home/user/change.log</code> should match their appearance in <code>/home/user/updated.conf</code>. 

Example of output (if the added line is <code>setting4=true</code>): 
<pre>
ADDED: setting4=true
</pre>

Do not add extra blank lines. Save the changelog to <code>/home/user/change.log</code> for audit purposes.
