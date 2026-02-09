# Bug Report

### Describe the bug

Optional chaining expressions are being incorrectly evaluated for side effects. When using optional chaining (`?.`) in expressions, the code is not properly detecting whether the chained expression has side effects, leading to incorrect tree-shaking behavior.

### Reproduction

```js
// This should be included because the function call has side effects
const result = obj?.method();

// This should also be included
const value = obj?.prop?.anotherMethod();
```

When the above code is processed, expressions with optional chaining that should be preserved due to side effects are being removed or vice versa. The logic for determining whether a chain expression has effects appears to be inverted.

### Expected behavior

Optional chaining expressions should correctly evaluate whether they contain side effects. Expressions with side effects (like function calls) should be preserved during tree-shaking, while pure property accesses without side effects can be safely removed if unused.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
