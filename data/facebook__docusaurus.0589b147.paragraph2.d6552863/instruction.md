# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where paragraph elements are not being rendered correctly. It seems like the paragraph nodes are being created with the wrong structure, causing the content to either not display or throw errors during rendering.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxSource = `
This is a paragraph.

Another paragraph here.
`

const result = await compile(mdxSource)
// Paragraphs are not rendered correctly
```

When compiling MDX content that contains regular paragraphs, the output is malformed. The paragraph elements either don't appear in the final output or cause runtime errors when trying to render.

### Expected behavior

Paragraphs should be properly compiled and rendered as standard paragraph elements with their text content preserved. The AST nodes for paragraphs should have the correct type and structure to allow proper rendering.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
