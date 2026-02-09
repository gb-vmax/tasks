# Bug Report

### Describe the bug

I'm experiencing an issue with parsing default import specifiers in MDX files. When using default imports, the parser seems to be creating the wrong node type, which causes imports to not work as expected.

### Reproduction

```js
import React from 'react'
import MyComponent from './MyComponent'

// Default imports are being parsed incorrectly
```

When parsing MDX content with default imports, the resulting AST nodes have an incorrect type. Instead of being recognized as `ImportDefaultSpecifier` nodes, they're being treated as regular `ImportSpecifier` nodes.

### Expected behavior

Default import statements should be parsed correctly and produce `ImportDefaultSpecifier` nodes in the AST. The parser should properly distinguish between:
- `import Foo from 'bar'` (default import)
- `import { Foo } from 'bar'` (named import)

### Additional context

This appears to affect all default imports in MDX files. The issue seems related to how the parser handles the node type when finishing the parse operation for default import specifiers.

---
Repository: /testbed
