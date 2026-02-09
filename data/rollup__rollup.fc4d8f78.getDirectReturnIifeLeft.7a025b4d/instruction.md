# Bug Report

### Describe the bug

When using IIFE (Immediately Invoked Function Expression) patterns in generated code, the closing parenthesis is being placed incorrectly. This causes syntax errors in the generated JavaScript output.

### Reproduction

Generate code that uses a direct return IIFE pattern. The generated output will have malformed syntax where the IIFE invocation parentheses are not properly positioned.

Example of what's being generated (incorrect):
```js
(function(param) { return value }(
```

This results in invalid JavaScript that cannot be executed.

### Expected behavior

The IIFE should be properly formed with the invocation parentheses in the correct position:
```js
(function(param) { return value })()
```

### Additional context

This appears to affect code generation when creating immediately invoked function expressions with direct returns. The closing parenthesis for the function invocation is being included in the wrong part of the generated string, breaking the IIFE syntax.

---
Repository: /testbed
