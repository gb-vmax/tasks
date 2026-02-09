# Bug Report

### Describe the bug

I'm experiencing an issue with multi-expression handling where deoptimization isn't being applied correctly to all expressions. When I have multiple expressions in a sequence, it seems like some of them are being skipped during the deoptimization phase, which leads to incorrect optimization behavior.

### Reproduction

```js
// Create a multi-expression with 3 or more expressions
const multiExpr = new MultiExpression([expr1, expr2, expr3]);

// Deoptimize a path
multiExpr.deoptimizePath(['someProperty']);

// Expected: all expressions should be deoptimized
// Actual: only some expressions are deoptimized
```

The problem appears when there are multiple expressions in the sequence - the first expression never gets deoptimized, and depending on the number of expressions, some others might be skipped as well.

### Expected behavior

All expressions in a MultiExpression should have `deoptimizePath` called on them when deoptimizing a path. Currently, it looks like the first expression is always being skipped, which can lead to incorrect optimization assumptions downstream.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
