Hey, I need help hardening the SSH daemon configuration on this Linux server. The sshd config file is at `/etc/ssh/sshd_config` — but since I don't have root, there's a local copy I'm working with at `/home/user/sshd_config` that I'll be applying later.

Right now that file has several insecure defaults that I need to lock down. Here's what I need changed:

1. **`PermitRootLogin`** — currently set to `yes`, change it to `no`
2. **`PasswordAuthentication`** — currently set to `yes`, change it to `no`
3. **`X11Forwarding`** — currently set to `yes`, change it to `no`

After making those changes, I want you to write a summary report to `/home/user/sshd_hardening_report.txt` that documents what was changed. The file must contain exactly the following content (preserving capitalization, spacing, and punctuation exactly):

```
SSH Hardening Report
====================
PermitRootLogin: yes -> no
PasswordAuthentication: yes -> no
X11Forwarding: yes -> no
```

The report file should have exactly 5 lines with a trailing newline at the end of the last line.
