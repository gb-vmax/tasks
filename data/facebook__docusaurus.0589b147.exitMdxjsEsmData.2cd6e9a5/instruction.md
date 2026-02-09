# Bug Report

### Describe the bug

I'm encountering an issue with MDX ESM (EcmaScript Module) parsing where the data handler is being called incorrectly. When processing MDX files with ESM imports/exports, the parser seems to be passing the wrong context to the exit handler, which causes unexpected behavior during the parsing phase.

### Reproduction

```mdx
---
import { something } from './module'

export const config = {
  value: 'test'
}
---

# My MDX Content
```

When parsing MDX files with ESM statements like the above, the exit handler for ESM data receives an incorrect context object. This affects how the ESM blocks are processed and can lead to parsing errors or incorrect AST generation.

### Expected behavior

The ESM data exit handler should receive the proper token context, not the parser instance itself. The parser should correctly process ESM import/export statements and generate the appropriate AST nodes.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
