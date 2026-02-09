# Bug Report

### Describe the bug

I'm encountering an issue with MDX ESM import/export parsing where the exit handlers for `mdxjsEsm` nodes appear to be executing in the wrong order. This causes the AST transformation to fail or produce incorrect results when processing MDX files with ESM syntax.

### Reproduction

```mdx
---
export const metadata = {
  title: 'Example'
}

import { Component } from './component'
---

# My Document

Content here
```

When parsing this MDX content, the ESM blocks (imports/exports) are not being processed correctly. The data seems to be getting corrupted or lost during the markdown-to-AST conversion.

### Expected behavior

The ESM imports and exports should be properly parsed and included in the resulting AST structure. The exit handlers should process the node data before closing the node itself.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
