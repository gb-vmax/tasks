# Bug Report

### Describe the bug

I've encountered an issue where return statements in functions are being incorrectly marked as having side effects even when they should be ignored. This is causing unexpected behavior in dead code elimination.

### Reproduction

```js
function example() {
  return someExpression();
  unreachableCode(); // This should be eliminated
}
```

When the bundler processes this code, it seems to be evaluating side effects in the wrong order. The return statement's flow control (marking code as unreachable) should happen before checking if the return value has effects, but it appears to be happening after.

This means that in contexts where return statements should be ignored (like when `context.ignore.returnYield` is true), the broken flow isn't being set properly, leading to incorrect tree-shaking decisions.

### Expected behavior

Return statements should:
1. Mark the control flow as broken (making subsequent code unreachable)
2. Then check if the return value expression has side effects
3. Respect the `returnYield` ignore flag appropriately

The current behavior seems to have these steps in the wrong order, which affects how unreachable code is detected and removed.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
