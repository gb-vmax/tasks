# Bug Report

### Describe the bug

The `generateSnapshotStateMap` function is returning `null` instead of an empty object when no snapshot is provided. This causes issues when the return value is used in contexts expecting an object, leading to "Cannot read property of null" errors.

### Reproduction

```js
const result = generateSnapshotStateMap(null);

// Attempting to use the result as an object fails
Object.keys(result); // TypeError: Cannot convert undefined or null to object

// Or when spreading
const merged = { ...result, newKey: 'value' }; // TypeError
```

### Expected behavior

When `generateSnapshotStateMap` is called with `null`, it should return an empty object `{}` so that it can be safely used in object operations without additional null checks throughout the codebase.

### System Info
- Insomnia version: latest
- Platform: Cross-platform issue

---
Repository: /testbed
