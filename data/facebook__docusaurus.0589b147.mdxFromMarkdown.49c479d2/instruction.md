# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where ESM imports at the top of MDX files are not being recognized or processed correctly. The parser seems to be treating them as regular expressions instead of ESM statements.

### Reproduction

```mdx
import { Component } from './Component'

# My Document

<Component />
```

When parsing this MDX file, the import statement is not being handled properly. Instead of being recognized as an ESM import, it appears to be processed through the expression parser.

### Expected behavior

ESM imports should be correctly parsed and distinguished from MDX expressions. The `mdxjsEsmFromMarkdown()` handler should be invoked for import/export statements at the top level of MDX files.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
