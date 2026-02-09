# Bug Report

### Describe the bug

After a recent update, MDX content parsing seems to be broken. When trying to parse MDX documents, the content is not being processed correctly and the parser appears to skip or fail to handle the content chunks properly.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a paragraph with some content.
`

const result = await compile(mdxContent)
// Parser fails to process the content correctly
```

### Expected behavior

The MDX compiler should parse the content and generate the appropriate output. Content chunks should be properly entered and processed through the tokenization flow.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
