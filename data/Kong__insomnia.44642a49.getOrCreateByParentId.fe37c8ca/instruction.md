# Bug Report

### Describe the bug
After a recent update, I'm seeing unexpected behavior with gRPC request metadata timestamps. When accessing the same gRPC request multiple times in quick succession, the `lastActive` timestamp gets updated every single time, even when the accesses happen within milliseconds of each other.

### Reproduction
```js
// Get or create gRPC request metadata
const meta1 = await getOrCreateByParentId('request-123');
console.log(meta1.lastActive); // e.g., 1234567890000

// Immediately access again (within same millisecond/few milliseconds)
const meta2 = await getOrCreateByParentId('request-123');
console.log(meta2.lastActive); // Expected: 1234567890000, Actual: 1234567891000 (or similar, slightly incremented)
```

### Expected behavior
The `lastActive` timestamp should only update when there's a meaningful time gap between accesses (e.g., at least 1 second). Rapid consecutive calls to `getOrCreateByParentId` for the same parent should return the existing metadata without updating the timestamp unnecessarily.

This is causing issues with our activity tracking and making it difficult to determine when a request was actually last meaningfully accessed vs. just retrieved from the database.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
