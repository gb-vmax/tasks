# Bug Report

### Describe the bug

I'm encountering an issue with error reporting in the AST parser. When a parse error occurs, the error message and position information appear to be swapped or displayed incorrectly. The error output doesn't show the correct location where the parsing failed.

### Reproduction

```js
// Try parsing invalid syntax
const invalidCode = `
  function test() {
    let x = ;
  }
`;

// Parse the code
// Expected: Error at position X with message "Unexpected token"
// Actual: Error message shows position as the message and vice versa
```

### Expected behavior

When a parse error occurs, the error should display:
1. The correct position/line number where the error occurred
2. A meaningful error message describing what went wrong

Currently it seems like these two pieces of information are getting mixed up in the error output.

### System Info
- Latest version from main branch

---
Repository: /testbed
