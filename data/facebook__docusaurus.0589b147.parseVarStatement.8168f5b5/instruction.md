# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations in MDX files. When parsing variable statements (var/let/const), the parser seems to be producing incorrect AST nodes. The resulting syntax tree doesn't match what's expected for variable declarations.

### Reproduction

```js
// In an MDX file
const myVariable = 'test';
```

When this gets parsed, the AST node structure is malformed. The variable declaration node doesn't have the correct properties and the parser appears to be using the wrong argument when finalizing the node.

### Expected behavior

Variable declarations should be parsed correctly and produce valid AST nodes with all the proper properties (declarations, kind, etc.). The finalized node should represent a proper VariableDeclaration with the correct structure.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
