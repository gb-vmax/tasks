# Bug Report

### Describe the bug

I'm experiencing an issue with sequence expressions where only the last expression in a sequence is being deoptimized instead of all expressions. This appears to be causing incorrect optimization behavior when dealing with multiple expressions in a sequence.

### Reproduction

```js
// Example with sequence expression
const result = (expr1(), expr2(), expr3());

// When deoptimizePath is called, only expr2 and potentially expr3 
// are being processed, but expr1 is being skipped entirely
```

The problem seems to occur when there are multiple expressions that need to be deoptimized. The first expression in the sequence is never processed, which can lead to incorrect tree-shaking or optimization decisions.

### Expected behavior

All expressions in a multi-expression/sequence should have `deoptimizePath` called on them, not just a subset. Each expression could have side effects or dependencies that need to be tracked.

### System Info
- Rollup version: latest main branch
- Node version: 18.x

---
Repository: /testbed
