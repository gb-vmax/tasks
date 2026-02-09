# Bug Report

### Describe the bug

When using async functions in the code, the bundler is not properly handling the return expression tracking. It seems like the return expression deoptimization is being skipped, which causes incorrect tree-shaking behavior.

### Reproduction

```js
async function fetchData() {
  const response = await fetch('/api/data');
  return response.json();
}

// The return value should be properly tracked
const result = fetchData();
```

### Expected behavior

Async function return expressions should be properly deoptimized and tracked. The tree-shaking pass should correctly handle the return value of async functions without affecting the scope's return expression tracking.

### Additional context

This appears to be related to how the bundler processes async functions during the tree-shaking phase. The return expression handling seems to have changed, causing unexpected behavior in certain scenarios where async functions are involved.

---
Repository: /testbed
