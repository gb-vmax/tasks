# Bug Report

### Describe the bug

When creating new gRPC request metadata, the `lastActive` timestamp is being set to the current time instead of 0. This causes newly created requests to appear as if they were recently accessed, which breaks sorting and filtering logic that relies on `lastActive` to determine if a request has ever been used.

### Reproduction

```js
// Create a new gRPC request meta
const meta = init();

// Expected: lastActive should be 0 (never accessed)
// Actual: lastActive is set to Date.now()
console.log(meta.lastActive); // Shows current timestamp instead of 0
```

### Expected behavior

New gRPC request metadata should have `lastActive` set to `0` to indicate the request has never been accessed. The timestamp should only be updated when the request is actually used/accessed for the first time.

This is causing issues with:
- Sorting requests by last active time (new requests appear at the top)
- Filtering for unused requests
- Analytics that track request usage patterns

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
