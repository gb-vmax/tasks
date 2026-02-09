# Bug Report

### Describe the bug

I'm experiencing an issue with code generation where return statements are being generated incorrectly. The returned value appears after the semicolon instead of between `return` and the semicolon.

### Reproduction

When generating code for a return statement with an argument, the output is malformed:

```js
// Expected output:
return someValue;

// Actual output:
return;someValue
```

This causes syntax errors in the generated code since the value to be returned is placed after the semicolon, making it unreachable code instead of the return value.

### Steps to reproduce

1. Process MDX content that includes a return statement with a value
2. The generated JavaScript code will have the return value in the wrong position
3. The resulting code fails to execute properly

### Expected behavior

Return statements should be formatted as `return <value>;` with the value appearing between the `return` keyword and the semicolon.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
