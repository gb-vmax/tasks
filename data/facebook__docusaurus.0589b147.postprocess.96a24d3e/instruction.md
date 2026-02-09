# Bug Report

### Describe the bug

I'm experiencing an issue where MDX parsing seems to fail silently or return undefined results. When trying to parse MDX content, the parser doesn't return the expected events array and instead returns nothing.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test MDX document.
`

const result = await compile(mdxContent)
console.log(result) // Expected: compiled output, Actual: undefined or broken
```

### Expected behavior

The MDX compiler should return a properly processed result with all events from the parsing stage. The postprocessing step should return the processed events array so that subsequent compilation steps can work with it.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18+

---
Repository: /testbed
