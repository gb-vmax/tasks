# Bug Report

### Describe the bug

I'm experiencing an issue with optional chaining in call expressions where the bundler is incorrectly removing code that should be retained. When using optional chaining with a function call (`foo?.()`), if the callee evaluates to `null` or `undefined`, the code behaves unexpectedly.

### Reproduction

```js
const obj = {
  method: null
};

// This should short-circuit and not execute side effects
const result = obj.method?.();

// But side effects in the chain are being incorrectly handled
console.log('This should not print if method is null');
```

Another example:

```js
function maybeFunc() {
  return null;
}

// Optional call should skip the rest of the chain
const value = maybeFunc()?.();
// Expected: undefined
// Actual: code after this point may be incorrectly tree-shaken
```

### Expected behavior

When using optional chaining with call expressions, if the callee is `null` or `undefined`, the entire chain should short-circuit and return `undefined`. Any code that depends on this behavior should be preserved in the bundle.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to be related to how the bundler determines whether optional chains have side effects and whether subsequent code should be included or removed during tree-shaking.

---
Repository: /testbed
