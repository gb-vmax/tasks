# Bug Report

### Describe the bug

I'm experiencing an issue with member expression property resolution in computed vs non-computed scenarios. It seems like computed member expressions (bracket notation) are being incorrectly resolved, while non-computed ones (dot notation) work as expected.

### Reproduction

```js
const obj = {
  prop: 'value',
  'computed-prop': 'computed-value'
};

// This works fine (dot notation)
obj.prop

// This doesn't resolve correctly (bracket notation)
obj['computed-prop']
```

When using bracket notation to access properties, the property key resolution seems to be broken. The behavior suggests that computed member expressions are not being handled properly during the resolution phase.

### Expected behavior

Both dot notation and bracket notation should correctly resolve property keys. Computed member expressions using bracket notation should work the same way as non-computed member expressions using dot notation.

### Additional context

This appears to affect property access patterns where computed member expressions are used. The issue manifests when trying to resolve property keys dynamically.

---
Repository: /testbed
