# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations in MDX files. When parsing variable statements (var/let/const), the parser seems to be generating incorrect AST node types. The parsed output shows `VariableDeclarator` nodes where `VariableDeclaration` nodes should be expected.

### Reproduction

```jsx
// In an MDX file
const myVariable = 'test';
let anotherVar = 123;
var oldStyle = true;
```

When processing these declarations, the AST structure is malformed. The node type returned doesn't match what tools expecting standard JavaScript AST structure would anticipate.

### Expected behavior

Variable declarations should be parsed as `VariableDeclaration` nodes in the AST, consistent with standard JavaScript/ESTree specifications. The current behavior breaks compatibility with tools that traverse or transform the AST.

### Additional context

This appears to affect all types of variable declarations (var, let, const) in MDX content. The issue likely impacts any tooling that relies on proper AST node types for code analysis or transformation.

---
Repository: /testbed
