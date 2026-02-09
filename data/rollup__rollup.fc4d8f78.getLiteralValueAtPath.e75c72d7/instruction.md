# Bug Report

### Describe the bug

Logical expressions (`&&` and `||`) are producing incorrect results when evaluating literal values. The behavior seems inverted - expressions that should be optimized to truthy values are being treated as falsy and vice versa.

### Reproduction

```js
// Using || operator with falsy right-hand side
const result1 = false || someValue;
// Expected: Should handle falsy case correctly
// Actual: Being treated as if it's truthy

// Using && operator with truthy right-hand side  
const result2 = true && someValue;
// Expected: Should handle truthy case correctly
// Actual: Being treated as if it's falsy
```

The issue appears when the bundler tries to determine literal values for optimization purposes. The logical operators seem to have their behavior swapped - `&&` is behaving like `||` and `||` is behaving like `&&`.

### Expected behavior

- For `||` operator: When the right side is falsy, it should return `UnknownFalsyValue`
- For `&&` operator: When the right side is truthy, it should return `UnknownTruthyValue`

Currently these seem to be reversed, causing incorrect optimizations during the build process.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
