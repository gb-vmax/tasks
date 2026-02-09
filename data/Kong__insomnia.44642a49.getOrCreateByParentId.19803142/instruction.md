# Bug Report

### Describe the bug
After a recent update, gRPC request metadata seems to be disappearing unexpectedly. When I open a gRPC request that I haven't used in a while, all my previously saved metadata (like selected methods, request bodies, etc.) is gone and I have to reconfigure everything from scratch.

### Reproduction
1. Create a gRPC request and configure it with some metadata (method selection, request body, etc.)
2. Don't use that request for a few months
3. Open the request again
4. All the metadata is gone and the request appears as if it was just created

This is really frustrating because I have to reconfigure all my gRPC requests every time I come back to a project after a break.

### Expected behavior
The metadata for gRPC requests should persist indefinitely (or at least until manually deleted), regardless of how long it's been since the request was last accessed.

### Additional context
This seems to have started happening recently. I'm not sure if this is related to some cleanup logic or if it's unintentional. It's particularly problematic for requests that are only used occasionally or seasonally.

---
Repository: /testbed
