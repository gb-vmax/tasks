# Bug Report

### Describe the bug

I'm experiencing an issue with response retrieval in Insomnia where the application seems to be returning cached/stale response data instead of the most recent responses from the database. When I make multiple requests in quick succession, sometimes I see old response data being displayed even though new responses should have been created.

### Reproduction

Steps to reproduce:
1. Make a request to any endpoint
2. Modify the request slightly (e.g., change a parameter)
3. Make the same request again immediately
4. Check the response history

Sometimes the response list shows outdated data or doesn't reflect the most recent response that was just created. This seems to happen more frequently when making requests rapidly within a few seconds of each other.

### Expected behavior

The application should always show the most recent responses from the database, not cached versions. Each new request should immediately appear in the response history without any stale data being displayed.

### System Info
- Insomnia version: Latest
- OS: Various (reproduced on multiple systems)

This is affecting my workflow as I can't reliably see the latest responses when testing APIs. Any help would be appreciated!

---
Repository: /testbed
