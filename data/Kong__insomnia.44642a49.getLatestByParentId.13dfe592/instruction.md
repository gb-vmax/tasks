# Bug Report

### Describe the bug

When trying to retrieve the latest version of a request, I'm getting the oldest version instead. It seems like `getLatestByParentId` is returning versions in the wrong order.

### Reproduction

```js
// Create multiple versions of a request
await createRequestVersion(request); // version 1
await createRequestVersion(request); // version 2  
await createRequestVersion(request); // version 3

// Try to get the latest version
const latest = getLatestByParentId(request._id);

// Expected: version 3
// Actual: version 1
```

### Expected behavior

`getLatestByParentId` should return the most recently modified version, not the oldest one. This is breaking version history functionality where we need to access the latest state of a request.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
