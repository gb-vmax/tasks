# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the document flow initialization seems to be processing operations in the wrong order. When parsing certain MDX content, I'm getting unexpected behavior where container exits happen before content is fully consumed, leading to malformed output or parse errors.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Heading

Some content here

---

More content after divider
`

const result = await compile(mdxContent)
// Parser throws or produces unexpected output
```

The issue appears when the parser encounters null/end-of-file markers while processing flow content. The operations seem to execute in an incorrect sequence, causing the document structure to be invalid.

### Expected behavior

The parser should properly handle end-of-file scenarios by:
1. Consuming the null code
2. Closing any open flow contexts
3. Exiting containers in the correct order

Instead, it seems like containers are being exited before the content is properly consumed, which breaks the parsing state.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
