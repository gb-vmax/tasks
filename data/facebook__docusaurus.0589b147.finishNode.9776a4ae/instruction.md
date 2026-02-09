# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where node positions are being set incorrectly. When parsing MDX content, the end position of AST nodes seems to be pointing to the wrong location in the source text, which is causing downstream tools that rely on accurate source positions to fail.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

Some text here.
`

const result = await compile(mdxContent, {
  // ... options
})

// Check the AST node positions
// The end positions are incorrect - they point to the start of tokens instead of the end
```

### Expected behavior

AST nodes should have accurate `end` position information that points to the actual end of the node in the source text, not the start position. This is important for:
- Source maps
- Error reporting
- Code transformation tools
- Syntax highlighting

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken position-based tooling that was working before. Any help would be appreciated!

---
Repository: /testbed
