# Bug Report

### Describe the bug

I'm encountering an issue with MDX ESM parsing where the parser seems to hang or behave incorrectly when processing ESM import/export statements. The parsing doesn't complete as expected and appears to get stuck in an infinite loop or incorrect state.

### Reproduction

```mdx
import { something } from 'module'

# Content here

export const data = { foo: 'bar' }
```

When parsing MDX files with ESM statements like the above, the parser doesn't properly handle the transitions between data and line breaks, causing unexpected behavior.

### Expected behavior

The parser should correctly process ESM import/export statements in MDX files, properly exiting the data state before moving to line start handling. The file should parse without hanging or getting stuck.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
