# Bug Report

### Describe the bug

The `typeof` operator is returning incorrect values when used in constant folding/optimization. Instead of returning the actual type of a value, it appears to be converting values to strings first and then returning `"string"` for all cases.

### Reproduction

```js
// Example code that demonstrates the issue
const result1 = typeof 42;        // Should be "number", but returns "string"
const result2 = typeof true;      // Should be "boolean", but returns "string"  
const result3 = typeof undefined; // Should be "undefined", but returns "string"
const result4 = typeof null;      // Should be "object", but returns "string"
```

When the bundler optimizes these expressions, all `typeof` operations are incorrectly evaluated as `"string"` instead of their correct types.

### Expected behavior

The `typeof` operator should return the correct type string for each value:
- `typeof 42` → `"number"`
- `typeof true` → `"boolean"`
- `typeof undefined` → `"undefined"`
- `typeof null` → `"object"`
- etc.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started recently and is affecting constant folding optimizations during the build process.

---
Repository: /testbed
