# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where position information for AST nodes appears to be incorrect. When parsing MDX content, the `range` property on nodes seems to have incorrect values, and I'm also seeing cases where nodes have position data even when they shouldn't.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

Some text here with **bold** content.
`

const result = await compile(mdxContent)

// The AST nodes have incorrect range values
// Expected: range[0] should be start offset, range[1] should be end offset
// Actual: Both range values are the same (end offset appears twice)
```

### Expected behavior

- The `range` property should be `[startOffset, endOffset]` with two different values representing the start and end positions
- Position data should only be set when both start AND end offsets are properly defined

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken position tracking for syntax highlighting and error reporting in my editor integration. Any help would be appreciated!

---
Repository: /testbed
