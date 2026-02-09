# Bug Report

### Describe the bug

I'm encountering an issue with the `unist-util-visit` module where the `SKIP` export is not working as expected. Instead of getting the actual `SKIP` constant value, it appears to be returning a function.

### Reproduction

```js
const { SKIP } = require('./jest/vendor/unist-util-visit@5.0.0.js');

console.log(typeof SKIP); // Expected: 'symbol' or 'string', Actual: 'function'

// This breaks when trying to use SKIP in visitor functions
const visitor = (node) => {
  if (shouldSkip(node)) {
    return SKIP; // This now returns a function instead of the constant
  }
};
```

### Expected behavior

`SKIP` should be exported as a constant value (likely a symbol or string), not as a function. This is breaking code that relies on comparing the return value with the `SKIP` constant.

### Additional context

This seems to have been introduced in a recent change to the vendored unist-util-visit module. The `CONTINUE` and `EXIT` exports work fine, but `SKIP` has different behavior.

---
Repository: /testbed
