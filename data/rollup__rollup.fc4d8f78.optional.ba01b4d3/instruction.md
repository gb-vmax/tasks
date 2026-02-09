# Bug Report

### Describe the bug

I'm encountering an issue with optional chaining on call expressions. When setting the `optional` property on a `CallExpression` node, the behavior seems inverted - setting it to `true` makes it `false` and vice versa.

### Reproduction

```js
const callExpr = new CallExpression(/* ... */);

// Setting optional to true
callExpr.optional = true;
console.log(callExpr.optional); // Expected: true, Actual: false

// Setting optional to false  
callExpr.optional = false;
console.log(callExpr.optional); // Expected: false, Actual: true
```

### Expected behavior

When `callExpr.optional = true` is set, the getter should return `true`. Currently it returns the opposite value of what was assigned.

This is breaking optional chaining detection in my AST transformations - expressions that should be marked as optional (`foo?.()`) are not being flagged correctly, and non-optional calls are incorrectly marked as optional.

### System Info
- Rollup version: latest main branch
- Node version: 18.x

---
Repository: /testbed
