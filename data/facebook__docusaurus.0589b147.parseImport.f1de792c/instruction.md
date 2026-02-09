# Bug Report

### Describe the bug

I'm experiencing an issue with import statement parsing in MDX files. When using simple string imports (like `import 'some-module'`), the AST node structure appears to be malformed. The `finishNode` call seems to be happening at the wrong time, which causes the source property to be set after the node is already marked as finished.

### Reproduction

```js
// This type of import statement causes issues
import 'styles.css'
import 'normalize.css'

// Regular imports with specifiers work fine
import React from 'react'
import { useState } from 'react'
```

When parsing MDX content with bare import statements (imports without specifiers), the parser seems to finalize the ImportDeclaration node prematurely before setting all required properties.

### Expected behavior

Both types of import statements should be parsed correctly and produce valid AST nodes with all properties properly set before the node is finalized.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is causing issues when processing MDX files that include CSS imports or other side-effect imports. The parsing completes but the resulting AST structure doesn't match what's expected for proper import declarations.

---
Repository: /testbed
