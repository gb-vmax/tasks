# Bug Report

### Describe the bug

When calling functions with side effects in the first argument position, those side effects are being incorrectly ignored during tree-shaking. This causes functions with important side effects to be removed from the bundle even though they should be preserved.

### Reproduction

```js
function withSideEffect() {
  console.log('This should be preserved');
  return 42;
}

function pureFunction(a, b) {
  return a + b;
}

// The side effect in the first argument is not detected
pureFunction(withSideEffect(), 10);
```

After bundling, the call to `withSideEffect()` gets removed from the output even though it has side effects that should be preserved.

### Expected behavior

All function arguments should be checked for side effects, including the first argument. The side effect should be detected and the code should be preserved in the bundle.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
