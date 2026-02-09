# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the parser seems to get stuck in an infinite loop when processing certain content. The browser tab becomes unresponsive and eventually crashes.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

Some text content here.
`

// This causes the parser to hang
await compile(mdxContent)
```

When I try to compile even simple MDX content, the process never completes and the CPU usage spikes to 100%. I have to force quit the browser/Node process.

### Expected behavior

The MDX content should compile successfully without hanging or causing infinite loops.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x
- Browser: Chrome/Firefox (both affected)

This seems to have started happening recently. Any help would be appreciated!

---
Repository: /testbed
