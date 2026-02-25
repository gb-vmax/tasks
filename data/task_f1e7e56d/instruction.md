You are a cloud architect migrating legacy scripts to a new environment. You discover that the file <code>/home/user/scripts/deploy.sh</code> is sensitive, as it contains plain text credentials and must not be readable by users other than the owner. The file currently has permissions that allow group and others to read it. 

Your task is to restrict access to this file so that only the file owner has read and write permissions, and no other user or group has any access to the file. 

To verify this is done correctly, generate a log file at <code>/home/user/permission_check.log</code> in the following exact format (replace &lt;PERMISSIONS&gt; with the actual 10-character mode string):

<pre>
/home/user/scripts/deploy.sh permissions: &lt;PERMISSIONS&gt;
</pre>

For example, if the permissions are set correctly, the log might show:

<pre>
/home/user/scripts/deploy.sh permissions: -rw-------
</pre>

Do not include any extra text or characters in the log other than the line above. Ensure all steps are performed from the terminal, and that the output file is saved at <code>/home/user/permission_check.log</code> in plain text.
