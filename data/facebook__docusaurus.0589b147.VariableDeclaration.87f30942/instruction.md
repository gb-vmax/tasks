# Bug Report

### Describe the bug

After a recent update, variable declarations in generated code are missing semicolons. This is causing issues when the generated JavaScript is minified or concatenated with other code, leading to syntax errors in production builds.

### Reproduction

When using MDX to generate JavaScript output, variable declarations like `const`, `let`, or `var` are no longer followed by semicolons:

```js
// Expected output:
const foo = 'bar';

// Actual output:
const foo = 'bar'
```

This becomes a problem when the code is minified or when multiple statements are on the same line, causing unexpected behavior or syntax errors.

### Steps to reproduce:
1. Process an MDX file that generates variable declarations
2. Check the generated JavaScript output
3. Notice that variable declarations are missing trailing semicolons

### Expected behavior

Variable declarations should include semicolons at the end to ensure proper JavaScript syntax and prevent issues during minification or code concatenation.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
