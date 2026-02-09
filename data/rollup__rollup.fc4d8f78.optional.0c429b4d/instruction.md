# Bug Report

### Describe the bug

I'm experiencing an issue with optional chaining in call expressions. When setting the `optional` property on a CallExpression node, the behavior is inverted - setting it to `true` makes it `false` and vice versa.

### Reproduction

```js
const callExpr = new CallExpression(/* ... */);

// Try to mark the call as optional
callExpr.optional = true;

// Expected: callExpr.optional === true
// Actual: callExpr.optional === false

// Similarly, setting to false makes it true
callExpr.optional = false;
// callExpr.optional is now true
```

### Expected behavior

When setting `callExpr.optional = true`, the call expression should be marked as optional (e.g., `foo?.()` syntax). When setting it to `false`, it should be marked as non-optional.

Currently, the behavior is completely backwards - assigning `true` results in `false` and assigning `false` results in `true`.

### System Info
- Rollup version: latest from main branch
- Node version: 18.x

---
Repository: /testbed
