# Bug Report

### Describe the bug

I'm encountering an issue with parsing variable declarations that have multiple declarators. When I try to parse code with comma-separated variable declarations, the parser seems to be handling them incorrectly.

### Reproduction

```js
// This type of code is not being parsed correctly
const a = 1, b = 2, c = 3;

// Also affects let and var declarations
let x = 10, y = 20;
var foo = 'bar', baz = 'qux';
```

When parsing code with multiple variable declarations separated by commas, the resulting AST appears to be malformed or incomplete. The declarations array doesn't contain all the expected declarators.

### Expected behavior

The parser should correctly handle comma-separated variable declarations and produce an AST with all declarators properly included in the `declarations` array of the VariableDeclaration node.

### Additional context

This affects all variable declaration types (const, let, var) when they have multiple declarators. Single variable declarations seem to work fine, but as soon as there's a comma and additional declarators, things break.

---
Repository: /testbed
