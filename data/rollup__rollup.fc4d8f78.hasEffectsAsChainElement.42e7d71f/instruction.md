# Bug Report

### Describe the bug

Optional chaining with call expressions is not working correctly when the callee evaluates to `null` or `undefined`. The bundler is not properly handling the short-circuit behavior in these cases.

### Reproduction

```js
const obj = {
  method: null
};

// This should short-circuit and return undefined
const result = obj.method?.();

// But the code is being processed incorrectly
```

Another case:

```js
function test() {
  const fn = Math.random() > 0.5 ? () => 'hello' : null;
  
  // Optional chaining should prevent errors when fn is null
  return fn?.();
}
```

### Expected behavior

When using optional chaining with function calls (`?.()`) and the callee is `null` or `undefined`, the expression should:
1. Short-circuit and return `undefined`
2. Not evaluate any subsequent code in the chain
3. Not throw an error

Currently, it seems like the short-circuit behavior is not being properly detected or handled during the bundling process.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
