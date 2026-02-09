# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the position information in the AST nodes is completely wrong. After parsing MDX content, the `end` position of nodes seems to be pointing to the wrong location - it looks like it's using the start position instead of the end position.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdx = `
# Hello World

This is a test paragraph.
`

const result = await compile(mdx)

// When inspecting the AST, node positions are incorrect
// The end position shows values that don't match the actual end of the node
// It appears to be using start position data instead
```

### Expected behavior

The AST nodes should have accurate position information with `start` pointing to the beginning of the node and `end` pointing to the actual end of the node. This is critical for source maps, error reporting, and any tooling that relies on accurate position data.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is breaking our syntax highlighting and error reporting tools that depend on accurate position information from the parser.

---
Repository: /testbed
