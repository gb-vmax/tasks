# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions in my code where certain branches are being incorrectly included or excluded during tree-shaking. It seems like when I have a logical expression (like `&&` or `||`) with nested property accesses, the bundler is not properly determining which parts of the expression should be included in the final output.

### Reproduction

```js
// Example code that triggers the issue
const obj = {
  foo: {
    bar: true
  }
};

// Logical expression with property access
const result = obj.foo && obj.foo.bar;

// Expected: Both branches should be evaluated correctly for inclusion
// Actual: One branch seems to be incorrectly handled
```

When bundling code with logical expressions that have complex property paths, I'm seeing unexpected behavior where either:
- Properties that should be included are being tree-shaken out, or
- Properties that shouldn't be included are being kept in the bundle

This appears to happen specifically when the right-hand side of a logical expression contains property accesses that need to be tracked.

### Expected behavior

The bundler should correctly determine which parts of a logical expression need to be included based on the actual usage patterns. Both branches should be properly analyzed and included/excluded as appropriate.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
