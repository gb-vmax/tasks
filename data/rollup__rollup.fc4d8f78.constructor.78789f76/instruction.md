# Bug Report

### Describe the bug

I'm encountering an issue where `undefined` variables are being incorrectly identified or handled in the AST. When I reference `undefined` in my code, it seems to be treated as `null` instead, which is causing unexpected behavior in my application.

### Reproduction

```js
// Example code that triggers the issue
const x = undefined;

if (x === undefined) {
  console.log('This should print');
} else {
  console.log('But this prints instead');
}
```

When bundling code that uses `undefined`, the variable resolution appears to be incorrect. The AST seems to be treating `undefined` references differently than expected.

### Expected behavior

References to `undefined` should be properly recognized and handled as the `undefined` primitive value, not as `null` or any other value. The variable name should remain `'undefined'` throughout the AST processing.

### Additional context

This seems to affect how the bundler optimizes code that relies on checking for `undefined` values. Type checking and conditional logic that depends on `undefined` may not work correctly.

---
Repository: /testbed
