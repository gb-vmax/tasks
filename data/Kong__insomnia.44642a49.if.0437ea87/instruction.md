# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with request data not being updated correctly in the UI. When I modify a request (like changing the URL or headers), the changes don't seem to persist or reflect immediately. Sometimes the old data still shows up even after making updates.

### Reproduction

1. Open an existing request
2. Modify some properties (e.g., change the URL or add a header)
3. Save the changes
4. Navigate away and come back to the request
5. The old data sometimes appears instead of the updated values

Also seeing similar issues when deleting requests - sometimes the deleted request still appears in the list or can still be accessed.

### Expected behavior

When a request is updated, the new data should be immediately reflected everywhere in the application. Deleted requests should not be accessible anymore.

### Additional context

This seems to have started happening recently. The behavior is inconsistent - sometimes it works fine, other times the stale data persists. It's particularly noticeable when quickly making multiple changes to the same request.

---
Repository: /testbed
