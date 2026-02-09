# Bug Report

### Describe the bug

I'm experiencing an issue with throw statements in my code. After a recent update, code that appears after a throw statement is being included in the bundle when it shouldn't be. This is causing my bundle size to increase unnecessarily and potentially including dead code that should be eliminated.

### Reproduction

```js
function example() {
  throw new Error('Something went wrong');
  
  // This code should be tree-shaken as it's unreachable
  console.log('This should not be in the bundle');
  const unreachable = someExpensiveFunction();
  return unreachable;
}
```

When bundling this code, the unreachable statements after the throw are being included in the output bundle instead of being removed as dead code.

### Expected behavior

Code after a throw statement should be recognized as unreachable and removed during tree-shaking/dead code elimination. The bundle should not include any statements that come after a throw.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
