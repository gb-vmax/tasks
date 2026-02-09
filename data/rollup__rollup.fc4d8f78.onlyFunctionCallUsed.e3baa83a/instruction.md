# Bug Report

### Describe the bug

I'm experiencing an issue where functions are not being properly tree-shaken when they should be. It seems like unused function declarations/expressions are being included in the bundle even when they're never called.

### Reproduction

```js
// This function is never called anywhere
function unusedFunction() {
  console.log('This should be removed');
  return 42;
}

// Only this should remain in the bundle
export function usedFunction() {
  return 'used';
}
```

Expected: `unusedFunction` should be tree-shaken out of the bundle
Actual: `unusedFunction` is still present in the output

### Additional context

This seems to affect function declarations and function expressions assigned to variables. The bundler appears to be treating them as if they have side effects or are being used even when they're clearly not referenced anywhere in the code.

This is causing my bundle size to be larger than expected since dead code isn't being eliminated properly.

---
Repository: /testbed
