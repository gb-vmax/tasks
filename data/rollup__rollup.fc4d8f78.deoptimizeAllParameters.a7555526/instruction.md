# Bug Report

### Describe the bug

I'm experiencing an issue where function parameters beyond the first one are not being properly deoptimized during scope analysis. When a function has multiple parameters and they need to be deoptimized, only the first parameter gets deoptimized repeatedly, while the remaining parameters are completely ignored.

### Reproduction

```js
function example(param1, param2, param3) {
  // Some code that triggers deoptimization
  return arguments;
}
```

When the scope analyzer calls `deoptimizeAllParameters()` on this function:
- `param1` gets deoptimized multiple times (once for each parameter that exists)
- `param2` and `param3` are never deoptimized at all

This leads to incorrect optimization assumptions for parameters after the first one, which can cause issues with tree-shaking and dead code elimination.

### Expected behavior

All parameters should be deoptimized when `deoptimizeAllParameters()` is called, not just the first parameter. Each parameter should be marked as reassigned and have its path deoptimized exactly once.

### System Info

- Rollup version: latest main branch
- Node version: 18.x

---
Repository: /testbed
