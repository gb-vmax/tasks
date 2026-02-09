# Bug Report

### Describe the bug

I'm experiencing an issue where deoptimization doesn't seem to be working correctly for local variables. When a variable's path is deoptimized, the expressions that should be deoptimized appear to be cleared before they're actually processed, causing them to not get deoptimized at all.

### Reproduction

```js
// Create a local variable with expressions to be deoptimized
const variable = new LocalVariable(name, declarator, init);

// Add expressions that need deoptimization
variable.addExpressionToBeDeoptimized(expression1);
variable.addExpressionToBeDeoptimized(expression2);

// Trigger deoptimization with empty path
variable.deoptimizePath([]);

// Expected: expression1 and expression2 should have deoptimizeCache() called
// Actual: The expressions array is cleared before iteration, so nothing happens
```

### Expected behavior

When `deoptimizePath` is called with an empty path, all expressions in the `expressionsToBeDeoptimized` array should have their cache deoptimized before the array is cleared. Currently it seems like the array gets cleared first, which means the loop iterates over an empty array and no deoptimization actually happens.

### System Info
- Rollup version: latest main branch
- Node version: 18.x

This is affecting tree-shaking behavior in my project where certain side effects aren't being properly tracked after reassignment.

---
Repository: /testbed
