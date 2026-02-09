# Bug Report

### Describe the bug

I'm experiencing an issue with MDX processing where the footer is being added to the output even when there's no footer content. This is causing unexpected text nodes and footer elements to appear in the generated AST.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a simple MDX document without any footnotes or footer content.
`

const result = await compile(mdxContent)
// The output AST contains unexpected footer elements and newline text nodes
```

### Expected behavior

When there's no footer content (no footnotes, etc.), the output should not include any footer-related nodes. The AST should only contain the actual content from the MDX document.

Currently, it seems like the footer is being unconditionally added to the result, even when the `foot` variable is empty/undefined.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
