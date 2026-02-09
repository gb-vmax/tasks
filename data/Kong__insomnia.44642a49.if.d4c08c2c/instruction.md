# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with request data becoming stale in the application. When I modify a request (change headers, body, etc.) and then try to access it again, the application sometimes returns the old version of the request instead of the updated one.

### Reproduction

Steps to reproduce:
1. Create or open an existing request
2. Modify some properties (e.g., update a header value or change the request body)
3. Save the changes
4. Immediately access the same request by ID
5. The returned request data still shows the old values instead of the updated ones

This seems to happen inconsistently - sometimes the updates are reflected immediately, other times they're not. It appears to be more noticeable when making rapid changes to requests.

### Expected behavior

When I retrieve a request by ID, it should always return the most current version of that request from the database, reflecting any recent modifications.

### System Info

- Insomnia version: latest
- OS: macOS

This is causing problems in my workflow as I can't trust that the data I'm seeing is up-to-date. Has anyone else experienced this issue?

---
Repository: /testbed
