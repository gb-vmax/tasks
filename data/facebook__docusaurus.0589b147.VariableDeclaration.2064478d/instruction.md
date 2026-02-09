# Bug Report

### Describe the bug

I'm experiencing an issue with variable declarations in generated code. It looks like the semicolon is being placed before the variable declaration instead of after it, which results in invalid JavaScript syntax.

### Reproduction

When processing MDX files with variable declarations, the generated output produces malformed JavaScript:

```js
// Expected output:
const foo = 'bar';

// Actual output:
;const foo = 'bar'
```

This causes syntax errors when the generated code is executed. The semicolon appears to be in the wrong position - it's being written before the variable declaration rather than after it.

### Expected behavior

Variable declarations should have the semicolon placed after the declaration statement, not before it, to produce valid JavaScript syntax.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
