# Bug Report

### Describe the bug

I'm encountering an issue with MDX ESM imports where they're not being recognized when placed at the start of a file. It seems like ESM import/export statements that begin at column 1 are being rejected instead of parsed correctly.

### Reproduction

```mdx
import { Component } from './component'

# My Document

<Component />
```

The import statement at the beginning of the file is not being processed. If I add whitespace before the import, it works, but that's not valid ESM syntax.

### Expected behavior

ESM import/export statements should be recognized and parsed when they start at column 1 (the beginning of a line), which is the standard position for module-level imports and exports in JavaScript/MDX files.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
