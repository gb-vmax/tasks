# Bug Report

### Describe the bug
When processing MDX content, the tokenizer is returning events even when the chunk processing is incomplete. This causes the parser to incorrectly handle content that should still be buffered, leading to malformed output or parsing errors.

### Reproduction
```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test document with multiple chunks.
`

const result = await compile(mdxContent)
// Parser returns incomplete/incorrect results
```

### Expected behavior
The tokenizer should only return events when all chunks have been fully processed (i.e., when the last chunk is `null`). Currently it's returning events prematurely, which breaks the parsing flow.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to be affecting any MDX content that gets split into multiple chunks during tokenization. The parser is not waiting for the complete input before generating events.

---
Repository: /testbed
