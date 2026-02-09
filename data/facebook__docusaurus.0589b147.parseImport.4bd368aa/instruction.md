# Bug Report

### Describe the bug

Import statements without specifiers are not being parsed correctly. When using a simple import like `import "module"`, the source property ends up being empty instead of containing the module path.

### Reproduction

```js
// This type of import statement fails to parse correctly
import "some-module";

// The parsed AST node has:
// node.source = [] (empty array)
// instead of the expected module string
```

### Expected behavior

The parser should correctly capture the module path string in the `source` property of the ImportDeclaration node, even when there are no import specifiers.

For an import statement like `import "lodash"`, the resulting AST node should have:
- `specifiers`: empty array
- `source`: the string literal node containing "lodash"

### Additional context

This seems to affect side-effect imports (imports without any specifiers) specifically. Named imports and default imports appear to work fine.

---
Repository: /testbed
