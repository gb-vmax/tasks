# Bug Report

### Describe the bug

I'm experiencing an issue with snapshot state entries where the `key` property is sometimes returning a function instead of a string value. This is causing problems when trying to access or compare keys in the sync system.

### Reproduction

```js
// When creating a snapshot state entry
const entry = snapshotStateEntrySchema.key();

// Sometimes this returns a function instead of the expected string
console.log(typeof entry); // Expected: 'string', Got: 'function'
console.log(entry); // Expected: 'key', Got: [Function: toString]
```

### Expected behavior

The `key` property should always return a string value `'key'`, not a function reference. This is breaking key comparisons and serialization throughout the sync system.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
