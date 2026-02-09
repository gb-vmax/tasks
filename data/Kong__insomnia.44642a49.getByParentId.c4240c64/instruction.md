# Bug Report

### Describe the bug

I'm experiencing an issue where gRPC request metadata isn't being updated correctly in real-time. When I make changes to request metadata (like updating the lastActive timestamp or other fields), the changes don't seem to be reflected immediately in the UI or when I retrieve the metadata again.

### Reproduction

1. Open a gRPC request
2. Make some changes or interact with the request
3. Quickly switch to another request and back
4. The metadata appears stale - it shows old values instead of the updated ones

It seems like the metadata is being cached somewhere and not invalidating properly when updates happen. This is particularly noticeable when:
- Switching between multiple gRPC requests quickly
- Making updates to request metadata
- Expecting to see the latest `lastActive` timestamp

### Expected behavior

When metadata is updated (via `update()` or any other method), subsequent calls to retrieve that metadata should return the latest values, not cached/stale data.

### Additional context

This seems to have started happening recently. The metadata retrieval appears to be returning outdated information even though the underlying database has been updated.

---
Repository: /testbed
