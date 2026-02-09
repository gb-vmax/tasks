# Bug Report

### Describe the bug

I'm experiencing an issue with the `getById` function in the workspace model. When passing a valid workspace ID, the function is returning `undefined` instead of the actual workspace object.

### Reproduction

```js
// Assuming we have a workspace with ID 'wrk_123'
const workspace = getById('wrk_123');

// Expected: workspace object
// Actual: undefined
console.log(workspace); // undefined
```

The function works correctly when called without arguments or with `undefined`, but fails when passing an actual workspace ID string.

### Expected behavior

When calling `getById('wrk_123')` with a valid workspace ID, it should return the corresponding workspace object from the database. The function should only return `undefined` when the workspace doesn't exist or when called with `undefined`.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
