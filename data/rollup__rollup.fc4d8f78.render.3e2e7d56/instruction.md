# Bug Report

### Describe the bug

When using sequence expressions with multiple comma-separated values where some expressions are tree-shaken, the output code incorrectly removes trailing commas even when there are multiple remaining expressions.

### Reproduction

```js
// Input code with sequence expression
const result = (sideEffect1(), sideEffect2(), finalValue);

// When sideEffect1() gets tree-shaken but sideEffect2() and finalValue remain,
// the output incorrectly removes the comma between sideEffect2() and finalValue
```

This causes the generated code to have syntax errors or produce incorrect output when multiple expressions remain after tree-shaking.

### Expected behavior

When a sequence expression has multiple included nodes after tree-shaking, all necessary commas between the remaining expressions should be preserved. Only the trailing comma after the last expression should be removed.

For example, if we have `(a, b, c)` and `a` gets tree-shaken, the output should be `(b, c)` not `(b c)`.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
