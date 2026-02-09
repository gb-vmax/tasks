# Bug Report

### Describe the bug

When working with gRPC request metadata, I'm encountering issues with missing properties on newly created objects. It seems like the initialization is incomplete, and certain fields that should be present are undefined.

### Reproduction

```js
// Create a new gRPC request meta object
const meta = init();

// Expected properties are missing
console.log(meta.createdAt); // undefined
console.log(meta.activityCount); // undefined

// Only these properties exist:
console.log(meta.pinned); // false
console.log(meta.lastActive); // 0
```

### Expected behavior

The `init()` function should return a complete metadata object with all necessary properties initialized, including `createdAt` and `activityCount`. These properties appear to be missing from the initialization, which could cause issues when the code tries to access or update them later.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
