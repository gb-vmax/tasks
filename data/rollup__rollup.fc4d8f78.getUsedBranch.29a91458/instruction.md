# Bug Report

### Describe the bug

The logical AND operator (`&&`) is not correctly evaluating which branch to use during tree-shaking optimization. When the left side of an `&&` expression evaluates to a truthy value, the wrong branch is being selected for inclusion in the bundle.

### Reproduction

```js
// Input code
const value = true && someFunction();

// Expected: someFunction() should be included in the bundle
// Actual: someFunction() is being incorrectly tree-shaken out
```

Another example:

```js
const result = (1 + 1) && expensiveComputation();
// The right side should be evaluated/included, but it's being removed
```

### Expected behavior

For the `&&` operator:
- When the left operand is truthy, the right branch should be used/included
- When the left operand is falsy, the left branch should be used/included

Currently it seems like the opposite is happening - when the left side is truthy, the left branch is being selected instead of the right branch.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues with conditional imports and side effects that rely on `&&` expressions.

---
Repository: /testbed
