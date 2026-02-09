# Bug Report

### Describe the bug

I'm experiencing an issue with function parameter handling in the bundler. When a function uses default parameters or destructuring patterns, those parameters are not being included in the output bundle, causing runtime errors.

### Reproduction

```js
function test({ x = 5, y } = {}) {
  return x + y;
}

export { test };
```

After bundling, the function parameters with default values or destructuring patterns are missing from the output, leading to `undefined` errors when the function is called.

### Expected behavior

All function parameters, including those with default values and destructuring patterns, should be properly included in the bundled output. The function should work correctly at runtime regardless of the parameter type.

### Additional context

This seems to affect:
- Functions with destructured parameters
- Functions with default parameter values
- Functions with rest parameters

Simple identifier parameters appear to work fine, but any complex parameter pattern gets stripped out during the bundling process.

---
Repository: /testbed
