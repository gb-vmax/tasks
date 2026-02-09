# Bug Report

### Describe the bug

I'm experiencing an issue where literal values from function call expressions are not being resolved correctly. When trying to get the literal value at a path from a call expression that returns a known value, it's returning `UnknownValue` instead of the actual literal value.

### Reproduction

```js
// Example scenario:
function getValue() {
  return { prop: 'test' };
}

const result = getValue();
// Trying to access result.prop should resolve to 'test'
// but it's being treated as UnknownValue instead
```

This affects constant folding and tree-shaking optimizations where the bundler should be able to determine literal values from function calls with known return expressions.

### Expected behavior

When a call expression has a known return expression (not UNKNOWN_EXPRESSION), the bundler should be able to resolve literal values at paths correctly. The literal value should be extracted from the return expression rather than immediately returning UnknownValue.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
