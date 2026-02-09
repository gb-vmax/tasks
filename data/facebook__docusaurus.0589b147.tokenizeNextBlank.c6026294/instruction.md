# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where blank lines after ESM imports are not being handled correctly. The parser seems to be consuming characters in the wrong order and the blank line detection logic appears to be inverted.

### Reproduction

```mdx
import { something } from 'somewhere'

# Heading

Content here
```

When parsing MDX files with imports followed by blank lines and then content, the parser behaves unexpectedly. The blank line tokenization doesn't work as intended, causing issues with how the document structure is recognized.

### Expected behavior

The parser should correctly handle blank lines that appear after ESM import statements. The tokenizer should properly enter the "lineEndingBlank" state before consuming the code, and blank line detection should work in the correct order.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
