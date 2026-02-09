# Bug Report

### Describe the bug

After a recent update, MDX parsing seems to be broken. When trying to parse MDX content, the tokenizer is not being initialized correctly and parsing fails silently or produces incorrect results.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test MDX document.
`

// Parsing fails or produces unexpected output
const result = await compile(mdxContent)
```

### Expected behavior

The MDX content should be parsed correctly and the tokenizer should be initialized with the proper parameters in the correct order.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
