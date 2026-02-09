# Bug Report

### Describe the bug

I'm experiencing an issue with the output bundle proxy where deleting non-existent properties causes unexpected behavior with the internal `reservedLowercaseBundleKeys` set. When attempting to delete a property that doesn't exist in the target object, the lowercase key is still being removed from the reserved keys set, which can lead to incorrect state management.

### Reproduction

```js
const bundle = getOutputBundle({
  'MyFile.js': { /* ... */ }
});

// Try to delete a property that doesn't exist
delete bundle['NonExistent.js'];

// The reservedLowercaseBundleKeys set incorrectly removes 'nonexistent.js'
// even though it was never in the target object
```

Similarly, when setting properties on the bundle, the reserved keys are being added even when the set operation fails (e.g., when trying to set a property on a non-extensible object or when a setter returns false).

### Expected behavior

- The `deleteProperty` trap should only remove entries from `reservedLowercaseBundleKeys` if the property actually exists in the target object
- The `set` trap should only add entries to `reservedLowercaseBundleKeys` when the set operation succeeds

This ensures the internal tracking set stays in sync with the actual state of the bundle object.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
