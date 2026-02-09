# Bug Report

### Describe the bug

I'm experiencing an issue with import statement parsing in MDX files. When parsing import declarations, the order of operations seems incorrect, causing the `source` property to be set before `specifiers` are parsed in certain cases.

### Reproduction

```js
// This import statement causes issues
import { Component } from 'library';

// The parser seems to handle the source before properly setting up specifiers
// Leading to unexpected behavior in the AST
```

When parsing import statements with specifiers (named imports), the source and specifiers appear to be processed in the wrong order. This affects how the import declaration node is constructed.

### Expected behavior

Import declarations should have their specifiers parsed first, followed by the source module string. The AST node should be properly constructed with both properties set in the correct sequence.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
