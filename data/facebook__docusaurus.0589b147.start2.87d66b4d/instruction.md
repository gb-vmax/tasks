# Bug Report

### Describe the bug

ESM import/export statements are not being recognized when they appear at the start of a line in MDX files. The parser seems to reject valid ESM syntax that should be allowed at column 1.

### Reproduction

```mdx
import { Component } from './component'

# My Document

Some content here.
```

The import statement at the beginning of the file is not being parsed correctly. It appears that statements starting at column 1 are being rejected when they should be valid.

### Expected behavior

ESM import/export statements should be recognized and parsed correctly when they start at the beginning of a line (column 1). This is standard MDX syntax and should work without issues.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
