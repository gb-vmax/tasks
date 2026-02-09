# Bug Report

### Describe the bug

I'm experiencing an issue with MDX rendering where footnotes are being inserted without proper line breaks. The output is missing the newline character that should separate the main content from the footnotes section, causing them to run together.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Test Document

Some content with a footnote[^1].

[^1]: This is a footnote
`

const result = await compile(mdxContent)
// The footnote appears immediately after content without a line break
```

### Expected behavior

When footnotes are rendered, there should be a newline (`\n`) between the main content and the footnote section to properly separate them. Currently, the footnote text is being appended directly without any spacing.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
