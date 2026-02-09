# Bug Report

### Describe the bug

Optional chaining with function calls is not working correctly when the callee is nullish. The code is being incorrectly tree-shaken or side effects are not being properly tracked.

### Reproduction

```js
const obj = null;

// This should short-circuit and not throw, but behavior is incorrect
obj?.method();

// Also affects cases like:
const maybeFunc = getSomeFunction(); // returns null/undefined
maybeFunc?.();
```

When using optional chaining (`?.`) on function calls where the callee evaluates to `null` or `undefined`, the bundler doesn't handle the short-circuit behavior properly. The expression should skip execution when the callee is nullish, but instead the code seems to be treated as if it will always execute.

### Expected behavior

Optional chaining should properly short-circuit when the callee is `null` or `undefined`, and the bundler should correctly track this control flow for tree-shaking and side effect analysis.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
