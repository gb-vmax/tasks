# Bug Report

### Describe the bug
ESM imports/exports in MDX files are not being recognized when they appear at the start of a line (column 1). The parser seems to be rejecting valid ESM syntax that should be accepted.

### Reproduction
```mdx
import { Component } from './component'

# My Document

Content here...
```

The import statement above is not being parsed correctly. It appears the column position check is too strict and is preventing valid ESM statements from being processed.

### Expected behavior
ESM import/export statements at the beginning of a line (column 1) should be parsed and recognized correctly. This is standard MDX syntax and should work without issues.

### Additional context
This seems to affect any ESM statement (import, export) that starts at column 1. Moving the statement to column 2 or later might work around the issue, but that's not valid JavaScript/ESM syntax.

---
Repository: /testbed
