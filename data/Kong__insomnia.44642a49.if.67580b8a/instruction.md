# Bug Report

### Describe the bug
After a recent update, duplicating requests in Insomnia appears to be broken. When I try to duplicate a request (HTTP, WebSocket, or gRPC), nothing happens or the application behaves unexpectedly. It seems like the duplication logic got messed up somehow.

### Reproduction
1. Create any type of request (HTTP, WebSocket, or gRPC)
2. Right-click on the request and select "Duplicate"
3. The duplication either fails silently or doesn't work as expected

I've tried this with different request types and the issue is consistent across all of them.

### Expected behavior
When duplicating a request, a new copy of the request should be created with a new ID and appear in the request list. The duplicated request should have all the same properties as the original (headers, body, etc.) but with a fresh ID and timestamps.

### Additional context
This was working fine in the previous version. I noticed the issue right after updating to the latest release. It affects all request types - HTTP, WebSocket, and gRPC requests.

---
Repository: /testbed
