# Bug Report

### Describe the bug

I'm experiencing an issue where the first parameter in a function is not being marked as `alwaysRendered` when it should be. This is causing problems with parameter handling in my bundled output.

### Reproduction

```js
function myFunction(firstParam, secondParam, thirdParam) {
  // Only secondParam and thirdParam are marked as alwaysRendered
  // firstParam is being skipped
  return firstParam + secondParam + thirdParam;
}
```

When bundling code with functions that have multiple parameters, the first parameter in each parameter list is not being processed correctly. The loop appears to be starting at index 1 instead of index 0, which means the first parameter is being ignored.

### Expected behavior

All parameters in the parameter list should be marked as `alwaysRendered`, including the first one. The current behavior skips the first parameter entirely.

### Additional context

This seems to have started happening recently. The parameter scope handling should iterate through all parameters, not skip the first one.

---
Repository: /testbed
