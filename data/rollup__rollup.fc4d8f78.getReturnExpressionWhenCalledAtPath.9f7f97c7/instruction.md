# Bug Report

### Describe the bug

I'm experiencing an issue where chained function calls are not being properly analyzed for side effects. When a function returns another function and that returned function is called, the bundler seems to be incorrectly determining whether the chain is pure or has side effects.

### Reproduction

```js
function outer() {
  console.log('outer called');
  return function inner() {
    console.log('inner called');
  };
}

// This call chain should be detected as having side effects
outer()();
```

The bundler appears to be making incorrect assumptions about the purity of the call chain. It seems like when the outer function returns something other than `UNKNOWN_EXPRESSION`, the analysis stops prematurely instead of continuing to check if the returned value itself has effects when called.

### Expected behavior

The bundler should correctly identify that both the outer function call and the chained inner function call have side effects (the console.log statements). The tree-shaking behavior should preserve these calls since they produce observable effects.

### System Info
- Rollup version: latest
- Node version: 18.x

This might be related to how the return expression tracking works when dealing with nested call expressions. The logic seems inverted - it's returning early when it should continue analyzing, and vice versa.

---
Repository: /testbed
