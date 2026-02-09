# Bug Report

### Describe the bug

I'm encountering a parsing issue with variable declarations in MDX files. When parsing JavaScript code that contains variable statements (var/let/const), the parser seems to be processing tokens in the wrong order, which causes syntax errors or unexpected parsing behavior.

### Reproduction

```js
// This should parse correctly but fails
const myVariable = 'test';

// Also affects:
let anotherVar = 123;
var oldStyle = true;
```

When trying to parse MDX content that includes these variable declarations, the parser throws errors or produces an incorrect AST structure.

### Expected behavior

Variable declarations should be parsed correctly without errors. The parser should properly handle the token sequence for variable statements and produce a valid AST.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to be a regression as it was working in previous versions. The issue affects all types of variable declarations (const, let, var).

---
Repository: /testbed
