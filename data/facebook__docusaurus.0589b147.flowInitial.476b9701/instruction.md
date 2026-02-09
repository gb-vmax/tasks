# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where it crashes with a "flowInitial is not a function" error. This appears to be happening during the tokenization phase when processing MDX content.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test document.
`

// This throws an error
await compile(mdxContent)
```

The error occurs when the parser tries to initialize flow content parsing. It seems like `flowInitial` is being called as a function somewhere in the tokenization process, but it's not actually a function reference.

### Expected behavior

The MDX content should compile successfully without throwing any errors. The parser should be able to process basic markdown/MDX syntax without crashing.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
