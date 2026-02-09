# Bug Report

### Describe the bug

I'm encountering an issue with code generation where `return` statements are being formatted incorrectly. The generated JavaScript code has the semicolon appearing before the return value instead of after it.

### Reproduction

When processing code that contains return statements with values, the output is malformed:

```js
// Expected output:
return someValue;

// Actual output:
return; someValue 
```

This makes the generated code syntactically invalid - the semicolon terminates the return statement early, and the value expression becomes a separate statement.

### Expected behavior

Return statements should be generated with proper syntax:
- The `return` keyword
- A space
- The return value expression
- A semicolon at the end

The semicolon should come after the entire return expression, not immediately after the `return` keyword.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
