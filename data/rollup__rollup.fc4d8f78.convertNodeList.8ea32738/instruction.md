# Bug Report

### Describe the bug

I'm encountering an issue with AST parsing where the first element in node lists is being skipped or not properly converted. This appears to affect various AST node types that contain lists of child nodes.

### Reproduction

When parsing code that produces AST nodes with multiple children, the first child node in the list is consistently missing or undefined in the resulting AST structure. For example:

```js
// Input code with multiple statements/expressions
const code = `
  const a = 1;
  const b = 2;
  const c = 3;
`;

// After parsing, the AST is missing the first statement
// Expected: 3 statements in the body
// Actual: Only 2 statements, starting from the second one
```

This seems to affect any AST node that contains a list of child nodes - function parameters, array elements, object properties, statement lists, etc. The first item is always missing from the converted list.

### Expected behavior

All elements in node lists should be properly converted and included in the AST output. The first element should not be skipped.

### System Info
- Version: Latest from main branch
- Node.js: v18.x

---
Repository: /testbed
