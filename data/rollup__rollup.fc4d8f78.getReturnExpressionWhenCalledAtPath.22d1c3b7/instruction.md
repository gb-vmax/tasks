# Bug Report

### Describe the bug

I'm seeing incorrect tree-shaking behavior with conditional expressions when the test condition cannot be statically determined. Functions that have side effects are being incorrectly removed from the bundle.

### Reproduction

```js
const condition = Math.random() > 0.5;
const fn = condition ? sideEffectA : sideEffectB;
fn();
```

When the condition cannot be evaluated at build time, the code is being tree-shaken too aggressively. The function call should be preserved since we can't know which branch will be taken at runtime, but it's being removed as if it has no side effects.

This seems to happen specifically when:
1. The conditional expression's test cannot be statically evaluated
2. The result is called as a function
3. Both branches are functions with side effects

### Expected behavior

When a conditional expression's branches both contain functions with side effects and the condition cannot be determined at build time, the function calls should be preserved in the output bundle.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
