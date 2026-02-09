# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue when trying to parse MDX content. The parser seems to get stuck in an endless loop and eventually crashes with a stack overflow error.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a simple MDX document.
`

// This causes infinite recursion
await compile(mdxContent)
```

### Expected behavior

The MDX content should compile successfully without any errors. The parser should process the content and return the compiled output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The same code was working fine before. Any help would be appreciated!

---
Repository: /testbed
