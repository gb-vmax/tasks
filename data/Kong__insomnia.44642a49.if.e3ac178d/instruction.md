# Bug Report

### Describe the bug

When calling `getMostRecentlyModified()` on an empty database, the function returns `undefined` instead of returning `null` as expected. This breaks code that relies on the documented behavior of returning `null` when no documents are found.

### Reproduction

```js
// With an empty database
const result = await database.getMostRecentlyModified('Request', {});

console.log(result); // Expected: null, Actual: undefined
```

The issue occurs when the database is empty (`db._empty` is true). Instead of querying and returning `null` when no documents exist, the function now returns `undefined` early.

### Expected behavior

The function should return `null` when no matching documents are found, regardless of whether the database is empty or not. This is consistent with the documented API and prevents type errors in code that checks for `null` specifically.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
