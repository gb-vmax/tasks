# Bug Report

### Describe the bug

I'm experiencing an issue with property enumeration after a recent update. It appears that the first property in exported objects is not being enumerable, while subsequent properties are enumerable as expected.

### Reproduction

```js
// When exporting multiple properties
export { foo, bar, baz };

// Expected: all properties should be enumerable
// Actual: 'foo' is not enumerable, but 'bar' and 'baz' are
```

This is causing issues when iterating over exported properties or using methods like `Object.keys()` on the exported module object. The first property is consistently being skipped in enumeration.

### Expected behavior

All exported properties should have consistent enumerability. Either all properties should be enumerable or none should be, but there shouldn't be a difference between the first property and the rest.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
