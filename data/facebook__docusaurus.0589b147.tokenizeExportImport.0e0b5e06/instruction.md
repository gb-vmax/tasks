# Bug Report

### Describe the bug

I'm experiencing a critical parsing issue with MDX files that contain import/export statements. After a recent update, my MDX files are failing to parse and I'm getting errors related to acorn parsing.

The issue seems to occur when processing ESM import/export statements in MDX. The parser appears to be cutting off mid-execution and not completing the parsing logic properly.

### Reproduction

```mdx
import { Component } from './components'

export const metadata = {
  title: 'My Page'
}

# My Content

Some content here...
```

When trying to parse this MDX file, the parser fails to complete processing the import/export statements correctly. The issue appears to be related to how the parser handles the estree body and defined module specifiers.

### Expected behavior

MDX files with import/export statements should parse successfully without errors. The parser should properly handle the estree body and continue processing all statements.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest LTS

This is blocking my entire project since all my MDX files use imports. Any help would be greatly appreciated!

---
Repository: /testbed
