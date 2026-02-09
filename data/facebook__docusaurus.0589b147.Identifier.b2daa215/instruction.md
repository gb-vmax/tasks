# Bug Report

### Describe the bug

After a recent update, JavaScript identifiers are not being written correctly when generating code from AST nodes. Instead of outputting the identifier name as a string, it appears the entire node object is being written, which results in `[object Object]` appearing in the generated output.

### Reproduction

```js
// When processing an Identifier node like:
const identifierNode = {
  type: 'Identifier',
  name: 'myVariable'
}

// The generated output contains:
// [object Object]
// 
// Instead of the expected:
// myVariable
```

This affects any code generation that involves identifiers - variable names, function names, property access, etc.

### Expected behavior

When generating code from an AST, identifier nodes should output their `name` property as a string (e.g., `myVariable`, `functionName`, etc.), not the object representation.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
