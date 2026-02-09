# Bug Report

### Describe the bug

I'm experiencing an issue with dynamic imports where the source AST node appears to be undefined or not properly set when trying to access it during the compilation process. This seems to be causing problems with import resolution in certain edge cases.

### Reproduction

```js
// In a module that uses dynamic imports
const module = await import('./my-module.js');

// The import expression's source node is not accessible
// when the AST is being processed, leading to errors
// during the build phase
```

The issue occurs when the AST nodes are being parsed and the source property is accessed before it's properly initialized. This affects dynamic import expressions specifically.

### Expected behavior

The source AST node should be available and properly set when the import expression is parsed, allowing the build process to correctly resolve and handle dynamic imports.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
