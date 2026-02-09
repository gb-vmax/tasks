# Bug Report

### Describe the bug

I'm experiencing an issue with optional chaining in call expressions. When setting the `optional` property on a CallExpression node, the behavior seems inverted - setting it to `true` makes it behave as if it's `false` and vice versa.

### Reproduction

```js
const callExpr = new CallExpression(/* ... */);

// Setting optional to true
callExpr.optional = true;

// But the call expression behaves as if optional is false
console.log(callExpr.optional); // Expected: true, Actual: false
```

This is causing issues when parsing code with optional chaining like `obj?.method()` - the AST doesn't correctly represent whether the call is optional or not.

### Expected behavior

When `callExpr.optional = true` is set, the call expression should be marked as optional and `callExpr.optional` should return `true`.

### System Info
- Rollup version: latest from main branch
- Node version: 18.x

---
Repository: /testbed
