# Bug Report

### Describe the bug

I'm experiencing an issue with import statement parsing in MDX files. When I have a simple import statement like `import "something"`, the parser seems to be processing it incorrectly. The specifiers and source appear to be swapped or assigned to the wrong properties.

### Reproduction

```js
// This import statement gets parsed incorrectly
import "my-module"

// The parser seems to assign values to the wrong node properties
// Expected: specifiers should be empty, source should be "my-module"
// Actual: the behavior seems reversed
```

When parsing import statements without named imports (bare imports), the AST node structure doesn't match what I'd expect. The `specifiers` field contains data that should be in `source`, and vice versa.

### Expected behavior

For a bare import like `import "module"`, the parser should:
- Set `node.specifiers` to an empty array
- Set `node.source` to the string literal "module"

Instead, it seems like these are being assigned backwards.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This is breaking my MDX parsing pipeline and causing downstream issues with module resolution. Any help would be appreciated!

---
Repository: /testbed
