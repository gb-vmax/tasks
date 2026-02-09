# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where position information seems to be getting mixed up. When processing MDX content, the parser appears to be returning incorrect offset and index values for tokens, which is causing problems with source maps and error reporting.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

Some content here
`

const result = await compile(mdxContent, {
  development: true
})

// Position information in the AST nodes appears incorrect
// _index and _bufferIndex values seem swapped
// offset value is also wrong
```

### Expected behavior

The tokenizer should return accurate position information with:
- Correct `offset` values matching the actual byte offset in the source
- Proper `_index` and `_bufferIndex` values that correspond to their actual positions

Currently, these values appear to be swapped or using the wrong variables, leading to incorrect source mapping.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
