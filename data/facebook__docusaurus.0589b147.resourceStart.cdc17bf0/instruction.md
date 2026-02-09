# Bug Report

### Describe the bug

I'm experiencing an infinite loop issue when parsing MDX content with resource links. The parser seems to get stuck and never completes, causing the process to hang indefinitely.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello

[link text](https://example.com)
`

// This hangs indefinitely
await compile(mdxContent)
```

### Expected behavior

The MDX content should parse successfully and return the compiled output without hanging.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to happen specifically when there are links with resources (URLs) in the markdown. Plain text and other markdown elements work fine, but as soon as a link is included, the parser gets stuck.

---
Repository: /testbed
