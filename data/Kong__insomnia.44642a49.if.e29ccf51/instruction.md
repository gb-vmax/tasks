# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with request data not reflecting updates in the UI. When I modify a request (change headers, body, etc.) and then navigate away and back to it, sometimes the old cached version is displayed instead of the current state from the database.

### Reproduction

Steps to reproduce:
1. Open a request and modify some properties (e.g., add a header or change the URL)
2. Navigate to a different request
3. Navigate back to the original request
4. The request sometimes shows stale data from before the modification

This seems to happen intermittently, especially when switching between requests quickly. The data in the database appears to be correct (verified by restarting the app), but the in-memory state gets out of sync.

### Expected behavior

The request should always show the most up-to-date data from the database, regardless of how many times you navigate to and from it. Any modifications should be immediately visible when you return to the request.

### Additional context

This wasn't happening in previous versions. It seems like there might be some caching mechanism that's not being invalidated properly when requests are updated. The issue is most noticeable with WebSocket and gRPC requests, but I've also seen it with regular HTTP requests occasionally.

---
Repository: /testbed
