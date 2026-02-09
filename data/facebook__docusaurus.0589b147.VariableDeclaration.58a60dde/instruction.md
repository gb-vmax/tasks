# Bug Report

### Describe the bug

Variable declarations are being generated with incorrect syntax - the semicolon appears before the variable declaration instead of after it.

### Reproduction

When processing JavaScript/MDX files with variable declarations, the output code has malformed syntax:

```js
// Expected output:
const myVar = 'value';

// Actual output:
;const myVar = 'value'
```

This is causing syntax errors in the generated code. The semicolon is being written before the variable declaration statement rather than after it.

### Steps to reproduce

1. Process an MDX file containing variable declarations
2. Check the generated JavaScript output
3. Notice the semicolon placement is incorrect

### Expected behavior

Variable declarations should have the semicolon at the end of the statement, not at the beginning. The generated code should be valid JavaScript.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
