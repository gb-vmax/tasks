# Bug Report

### Describe the bug

I'm experiencing an issue with the output bundle handling where lowercase bundle keys are not being tracked correctly. It seems like the internal tracking mechanism for reserved lowercase keys has stopped working.

When generating output bundles, the system should maintain a set of reserved lowercase bundle keys to prevent collisions, but this tracking appears to be broken. The reserved keys set is no longer being returned when accessed.

### Reproduction

```js
const bundle = getOutputBundle({
  'MyFile.js': { /* ... */ },
  'AnotherFile.js': { /* ... */ }
});

// Try to access the reserved lowercase keys
const reserved = bundle[lowercaseBundleKeys];
// Expected: Set containing lowercase versions of bundle keys
// Actual: undefined or incorrect value
```

### Expected behavior

The output bundle proxy should maintain and return a set of reserved lowercase bundle keys when accessed via the `lowercaseBundleKeys` symbol. This is used internally to prevent case-insensitive filename collisions.

Currently it seems like the getter is not returning the correct reserved keys set, which could lead to issues with case-insensitive file systems or duplicate filename detection.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
