# Bug Report

### Describe the bug

I'm experiencing an issue with form path resolution where accessing nested values returns `undefined` when the parent value is `undefined` (but not `null`). The path getter seems to stop traversing too early when encountering `undefined` values in the chain.

### Reproduction

```js
const values = {
  user: undefined
};

// Trying to get a nested path
const result = getPath('user.name', values);
// Returns: undefined

// But if the parent is null instead:
const values2 = {
  user: null
};

const result2 = getPath('user.name', values2);
// Also returns: undefined
```

The behavior is inconsistent - it seems like `undefined` values in the path are not being handled the same way as `null` values, causing the traversal to break unexpectedly.

### Expected behavior

The path getter should handle both `null` and `undefined` values consistently when traversing nested paths. If a value in the chain is `undefined`, it should still attempt to continue the traversal or at least handle it gracefully.

### System Info
- @mantine/form version: latest
- Browser: Chrome

---
Repository: /testbed
