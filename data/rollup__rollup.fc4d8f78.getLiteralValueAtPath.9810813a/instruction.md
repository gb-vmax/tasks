# Bug Report

### Describe the bug

I'm encountering an issue where unary operators (like `!`, `void`, etc.) are not being evaluated correctly during the build process. It seems like literal value evaluation for unary expressions is broken, causing the bundler to fail to optimize simple expressions.

### Reproduction

```js
// Simple negation operator
const result = !true;  // Should be optimized to false
console.log(result);

// Void operator
const voidResult = void 0;  // Should be optimized to undefined
console.log(voidResult);

// Negation with truthy value
const negated = !someValue;
```

When bundling code with these unary expressions, they're not being properly evaluated at compile time. The optimizer should be able to determine the literal values for these simple cases, but it appears to be treating them as unknown values instead.

### Expected behavior

Unary operators should be properly evaluated during the optimization phase:
- `!true` should resolve to `false`
- `void 0` should resolve to `undefined`
- Other unary operations on literal values should compute their results

This worked fine in previous versions and seems to have regressed recently.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
