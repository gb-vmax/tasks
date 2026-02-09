# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where blank lines after ESM imports are not being handled correctly. The parser seems to be consuming line endings in the wrong order, which causes unexpected behavior when processing certain MDX documents.

### Reproduction

```mdx
import { something } from 'somewhere'

# Heading

Content here
```

When parsing this MDX content, the blank line between the import and the heading is processed incorrectly. The parser appears to be exiting the "lineEndingBlank" state before consuming the code, and the attempt callback order seems reversed.

### Expected behavior

Blank lines following ESM import statements should be properly tokenized and consumed. The parser should correctly handle the line ending and move to the next state without issues.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
