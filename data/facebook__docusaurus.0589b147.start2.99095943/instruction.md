# Bug Report

### Describe the bug

ESM imports/exports in MDX are no longer being recognized when they appear at the start of a line (column 1). The parser seems to be rejecting valid ESM syntax that should be allowed.

### Reproduction

```mdx
import { Component } from './component'

# My Document

This is some content.
```

The import statement at the beginning of the file is not being parsed correctly. It appears the parser is now checking if the column position is greater than or equal to 1 instead of greater than 1, which means it's rejecting statements that start at column 1 (the beginning of the line).

### Expected behavior

ESM import/export statements should be valid when they appear at the start of a line (column 1). The parser should only reject them if they appear in the middle of a line (column > 1).

For example, this should work:
```mdx
import foo from 'bar'
export const meta = { title: 'Test' }
```

But this should be rejected:
```mdx
Some text import foo from 'bar'  // <- invalid, not at start of line
```

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
