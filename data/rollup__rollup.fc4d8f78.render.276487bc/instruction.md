# Bug Report

### Describe the bug

I'm experiencing an issue with semicolon insertion in expression statements. When the code is rendered, semicolons are being added in the wrong position, causing syntax errors in the generated output.

### Reproduction

```js
// Input code (expression statement without trailing semicolon)
const result = someFunction()

// After rendering, the semicolon appears to be inserted incorrectly
// Expected: const result = someFunction();
// Actual: const result = someFunction;()
```

The semicolon is being placed one character too early, which breaks the generated code. This seems to happen specifically when expression statements don't already have a trailing semicolon.

### Expected behavior

When an expression statement is missing a semicolon, it should be appended at the correct position (after the expression ends), not before the last character of the statement.

### Additional context

This appears to affect the rendering of expression statements across the board. The generated code becomes syntactically invalid when semicolons are inserted at incorrect positions.

---
Repository: /testbed
