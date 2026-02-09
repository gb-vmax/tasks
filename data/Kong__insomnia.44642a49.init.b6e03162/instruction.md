# Bug Report

### Describe the bug
After a recent update, all gRPC requests are being initialized with `pinned: true` and `lastActive: 1` by default. This is causing unexpected behavior where newly created gRPC requests appear as if they were already pinned and previously accessed, even though they're brand new.

### Reproduction
```js
// Create a new gRPC request
const newRequest = init();

// Expected: pinned: false, lastActive: 0
// Actual: pinned: true, lastActive: 1
console.log(newRequest.pinned);     // true (should be false)
console.log(newRequest.lastActive); // 1 (should be 0)
```

### Expected behavior
New gRPC requests should initialize with:
- `pinned: false` (unpinned by default)
- `lastActive: 0` (no previous activity)

This was the behavior before and makes more sense for newly created requests. Now all new gRPC requests show up as pinned in the UI which is confusing.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
