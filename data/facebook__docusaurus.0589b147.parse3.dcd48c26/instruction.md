# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the parser configuration isn't being initialized correctly. When trying to parse MDX content, the constructs array appears to be using the wrong value, which causes parsing to fail or behave unexpectedly.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test MDX document.
`

// Parsing fails or produces unexpected results
const result = await compile(mdxContent, {
  extensions: [/* custom extensions */]
})
```

### Expected behavior

The parser should use the provided extensions configuration and properly initialize the constructs array. The MDX content should parse successfully with custom extensions applied.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
