# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where blank lines in ESM blocks are not being handled correctly. After a recent change, the parser seems to be incorrectly processing line endings in certain contexts, causing the exit event to never be triggered.

### Reproduction

```mdx
import { something } from 'somewhere'

export const config = {
  value: 'test'
}

# My Content

Some text here
```

When parsing this MDX content, the blank line handling appears to be broken. The parser enters the "lineEndingBlank" state but doesn't properly exit it, leading to unexpected behavior in the syntax tree.

### Expected behavior

The parser should correctly handle blank lines between ESM imports/exports and the rest of the MDX content. The "lineEndingBlank" token should be properly entered and exited, and the blank line attempt should follow the correct code path.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
