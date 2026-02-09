# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM blocks where the parsed AST structure seems incorrect. When using ES module imports/exports in MDX files, the estree data is being attached even when it shouldn't be, and it appears the wrong node in the stack is being referenced.

### Reproduction

```mdx
import { Component } from './component'

# My Document

Some content here
```

When parsing this MDX file, the ESM import block's AST node structure doesn't match what's expected. The estree data appears to be attached to nodes incorrectly, causing downstream parsing issues.

### Expected behavior

The ESM block should be properly parsed with the correct node structure. The estree data should only be attached when an estree object is actually present from the tokenizer, and it should be attached to the correct node in the stack.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
