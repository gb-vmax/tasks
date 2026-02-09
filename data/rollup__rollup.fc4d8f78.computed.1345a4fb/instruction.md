# Bug Report

### Describe the bug

I'm experiencing an issue with member expression handling where computed property access is being incorrectly identified. When using bracket notation to access object properties (e.g., `obj['property']`), the code seems to be treating them as non-computed member expressions, which leads to incorrect behavior during compilation.

### Reproduction

```js
const obj = {
  foo: 'bar',
  baz: 'qux'
};

// Bracket notation should be treated as computed
const key = 'foo';
const value = obj[key];  // This is being misidentified

// Also affects dynamic property access
const prop = 'baz';
console.log(obj[prop]);  // Should work but behaves unexpectedly
```

### Expected behavior

Bracket notation member expressions should be correctly identified as computed property access. The distinction between `obj.property` (non-computed) and `obj['property']` (computed) should be properly maintained.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems to have started recently, possibly after a recent update. The logic for determining whether a member expression is computed appears to be inverted somehow.

---
Repository: /testbed
