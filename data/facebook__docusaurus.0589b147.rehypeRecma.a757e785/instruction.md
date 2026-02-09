# Bug Report

### Describe the bug

The MDX compiler is hanging/freezing when processing documents. The build process never completes and eventually times out or runs out of memory.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxSource = `
# Hello World

This is a simple MDX document.
`

// This call never returns
await compile(mdxSource)
```

### Expected behavior

The MDX document should compile successfully and return the compiled output without hanging.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The process just hangs indefinitely when trying to compile any MDX content.

---
Repository: /testbed
