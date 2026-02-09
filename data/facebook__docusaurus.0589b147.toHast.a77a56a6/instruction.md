# Bug Report

### Describe the bug

I'm experiencing an issue with MDX rendering where footnotes are appearing in the output even when they shouldn't be present. It seems like the footnote section is being added to documents that don't contain any footnotes.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a simple document without any footnotes.
`

const result = await compile(mdxContent)
// The output includes an unexpected footnote section
```

When I compile MDX content that doesn't have any footnotes, I'm seeing extra whitespace and a footnote section being added to the rendered output. This is causing layout issues in my application.

### Expected behavior

Documents without footnotes should not have a footnote section appended to them. The output should only contain the actual content from the MDX source.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
