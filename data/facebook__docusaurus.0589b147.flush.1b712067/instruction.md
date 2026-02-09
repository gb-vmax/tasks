# Bug Report

### Describe the bug

I'm experiencing an issue with HTML entity parsing where text content is not being properly flushed/output. It seems like the parser is skipping over regular text segments when processing entities.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
Hello &amp; world
`

const result = await compile(mdxContent)
// Expected: Output should contain "Hello & world"
// Actual: Text segments appear to be missing or empty
```

When parsing content with HTML entities, the text between entities or after entities doesn't appear in the output as expected. The flush mechanism seems to be inverted - it's only executing when the queue is empty instead of when there's content to flush.

### Expected behavior

Text content should be properly captured and included in the parsed output. All text segments, including those around HTML entities, should be preserved.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node.js version: 18.x

---
Repository: /testbed
