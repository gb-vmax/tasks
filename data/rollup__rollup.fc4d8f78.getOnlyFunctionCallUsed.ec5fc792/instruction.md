# Bug Report

### Describe the bug

I'm experiencing strange behavior with function call detection in my bundler setup. When checking if a variable is only used as a function call, the result seems to flip between true and false on subsequent checks, even though the actual usage hasn't changed.

### Reproduction

```js
// Given a variable that is only used as a function call
const myFunc = () => {};
myFunc();

// When checking if it's only used as function call multiple times
// First check returns the correct value
// Second check returns the opposite value
// Third check flips back again
```

The issue appears when the same variable is checked multiple times during the bundling process. Each time `getOnlyFunctionCallUsed()` is called, it returns a different result, which causes inconsistent tree-shaking behavior.

### Expected behavior

The function should return a consistent result indicating whether the variable is only used as a function call, regardless of how many times it's queried.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues with dead code elimination as the bundler can't reliably determine which functions are safe to optimize.

---
Repository: /testbed
