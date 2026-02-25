You are a Linux systems engineer asked to perform several hardening steps on user and permission management in a development environment. Complete all steps and document your actions as requested.

1. Create a new group called <b>devops</b> and a new user named <b>alice</b> who is a member of the <b>devops</b> group only (do not add alice to any other groups).
2. Set alice's login shell to <b>/bin/bash</b>. Set her home directory to <b>/home/alice</b>.
3. Secure alice's home directory so that only the user alice can read, write, or execute files in that directory (i.e., permissions 700).
4. In alice’s home directory, create a directory <b>/home/alice/projects</b>. Only alice and members of the devops group should be able to read, write, or execute in this directory (i.e., permissions 770, group ownership devops).
5. In <b>/home/alice</b>, create (or edit if it exists) a file named <b>security_notice.txt</b> with the exact contents:<br>
   <pre>
   SECURITY NOTICE:
   All access to this system is monitored.
   </pre>
   Set this file’s permissions to allow only owner read and write access (600).
6. Create a summary report file at <b>/home/user/hardening_log.txt</b> documenting exactly what steps you performed. The format of the log must match this example:<br>
   <pre>
   [STEP 1] Group 'devops' created.
   [STEP 2] User 'alice' created with group 'devops', home '/home/alice', shell '/bin/bash'.
   [STEP 3] Directory '/home/alice' permissions set to 700.
   [STEP 4] Directory '/home/alice/projects' created, permissions set to 770, group 'devops'.
   [STEP 5] File '/home/alice/security_notice.txt' created with owner-only permissions (600).
   </pre>
Complete all steps and ensure permissions and group ownerships are correctly set. Double-check that the contents of <b>/home/alice/security_notice.txt</b> and the log file exactly match the formats specified above, as automated tests will check for exact compliance.
