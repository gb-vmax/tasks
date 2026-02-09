# Bug Report

### Describe the bug

I'm experiencing a crash when trying to work with snapshot state maps in certain scenarios. The application throws a TypeError when `generateSnapshotStateMap` is called with specific input values.

### Reproduction

```js
const result = generateSnapshotStateMap(null);

// Expected: {}
// Actual: TypeError - Cannot read properties of null
```

When passing `null` to `generateSnapshotStateMap`, the function returns `null` instead of an empty object. This causes downstream code that expects an object to fail with type errors.

### Expected behavior

The function should return an empty object `{}` when given a `null` snapshot, allowing the rest of the code to handle it gracefully without type errors.

### System Info
- Version: Latest from main branch
- Node: 18.x

---
Repository: /testbed
