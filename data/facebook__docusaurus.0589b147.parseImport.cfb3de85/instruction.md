# Bug Report

### Describe the bug

I'm encountering an issue with import statement parsing in MDX files. When parsing import declarations, the `specifiers` and `source` properties appear to be getting swapped or assigned incorrectly.

### Reproduction

```js
// Simple import statement
import React from 'react';

// Named imports
import { useState, useEffect } from 'react';

// Side-effect import
import './styles.css';
```

When these imports are parsed, the resulting AST nodes have their `specifiers` and `source` properties mixed up. For example, with `import React from 'react'`, the source string ends up in the specifiers field and vice versa.

### Expected behavior

The parser should correctly assign:
- `node.specifiers` should contain the import specifiers (default, named, or empty array for side-effect imports)
- `node.source` should contain the module path string literal

Instead, these values are being swapped in the resulting ImportDeclaration nodes.

### System Info
- @mdx-js/mdx version: 3.0.0
- This affects all types of import statements (default, named, and side-effect imports)

---
Repository: /testbed
