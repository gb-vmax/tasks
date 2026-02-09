# Bug Report

### Describe the bug

I'm experiencing issues with MDX parsing when there are blank lines in the content. The parser seems to be handling blank line tokens incorrectly, causing unexpected behavior when processing MDX files with empty lines between content blocks.

### Reproduction

```mdx
import { Component } from './component'

<Component />

Some text here
```

When parsing MDX content that contains blank lines (especially after imports or JSX blocks), the parser doesn't handle them correctly. The content either fails to parse or produces malformed output.

### Expected behavior

Blank lines should be properly tokenized and handled during the parsing process. The MDX content should parse successfully regardless of blank lines between different content types (imports, JSX, markdown text).

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
