Hi, I'm an IT support technician and I have a ticket to resolve. Here's the situation:

We have a developer named `alice` who needs access to a shared project directory. The directory `/home/user/projects/webapp` already exists and is owned by the group `devteam`. Alice has been added to the system but was never added to the `devteam` group, so she can't access the project files. Additionally, there's a configuration file in the project that has incorrect permissions and needs to be fixed.

Here's what I need you to do:

**1. Add `alice` to the `devteam` group (as a supplementary group, keep her existing groups intact).**

**2. Fix the permissions on `/home/user/projects/webapp/config.cfg`:**
The file currently has overly permissive settings. It should be readable and writable by the owner, readable by the group, and have NO permissions for others. Set it to exactly mode `0640`.

**3. Write a brief resolution log to `/home/user/tickets/ticket_042.txt`** with the following exact content (fill in the bracketed parts with real values from the system):

```
Ticket: 042
Status: resolved
User: alice
Group added: devteam
Config file: /home/user/projects/webapp/config.cfg
Config permissions: 640
```

Each line must be exactly as shown above, with a newline at the end of the file. No trailing spaces, no extra blank lines.

Please take care of all three steps. The user `alice` and group `devteam` already exist on the system, so you don't need to create them.
</think>

Can you help me resolve this ticket?
