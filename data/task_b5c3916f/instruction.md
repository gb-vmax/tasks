You are a compliance analyst assigned to verify and generate an audit log of user access configurations on a Linux system. You are provided with an INI file located at <code>/home/user/configs/auth_config.ini</code> that defines user access levels to three services: <code>ssh</code>, <code>ftp</code>, and <code>http</code>. Each service section contains user names as keys and their access (either <code>allowed</code> or <code>denied</code>) as the values. 

Your goal is to:

1. Parse the INI file and extract, for each service, the names of all users who have <code>allowed</code> access.
2. For audit purposes, generate a plain text report at <code>/home/user/output/audit_user_access.log</code> listing, for each service, the users with allowed access. 
3. The report must have the following format:
  - For each service, output a section with the service name in uppercase inside square brackets (e.g., <code>[SSH]</code>).
  - List each allowed user for that service on a separate line directly under the section header.
  - No empty lines between sections or users.
  - The order of services must be: ssh, ftp, http (as sections); within each section, users must appear in lexicographical order.

For example, if the INI file contains:
<pre>
[ssh]
alice = allowed
bob = denied
felix = allowed

[ftp]
carol = allowed

[http]
bob = allowed
diana = denied
</pre>

The audit log should appear as:
<pre>
[SSH]
alice
felix
[FTP]
carol
[HTTP]
bob
</pre>

Your task is to produce this audit file according to the rules above, based on the current contents of <code>/home/user/configs/auth_config.ini</code>. Ensure the output matches the format exactly so it can be verified by an automated test.
