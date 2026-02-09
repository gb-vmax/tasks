# Bug Report

### Describe the bug
After a recent update, newly created gRPC request metadata is being initialized with the current timestamp instead of 0 for the `lastActive` field. This causes issues with sorting and filtering logic that expects fresh/unused requests to have a `lastActive` value of 0.

### Reproduction
```js
// Create a new gRPC request meta object
const meta = init();

// Expected: lastActive should be 0 for a newly created request
console.log(meta.lastActive); // Actual: prints current timestamp

// This breaks sorting logic that treats 0 as "never accessed"
// and causes new requests to appear as if they were recently used
```

### Expected behavior
The `lastActive` field should be initialized to 0 for new gRPC request metadata objects, indicating that the request has never been accessed. Only when the request is actually accessed/used should this field be updated to a timestamp.

This is important for:
- Properly sorting requests by last access time
- Identifying which requests have never been used
- Maintaining consistent behavior with other request types

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
