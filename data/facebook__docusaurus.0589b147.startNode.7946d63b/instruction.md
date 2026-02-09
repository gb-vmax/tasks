# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the parser seems to be creating nodes with incorrect position information. The parsed AST nodes are showing end positions instead of start positions, which is causing problems when trying to work with source locations in the parsed output.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxSource = `
# Hello World

Some content here.
`

const result = await compile(mdxSource)

// When inspecting the AST, nodes have incorrect position data
// The start position points to where the node ends, not where it begins
```

### Expected behavior

When parsing MDX content, each AST node should have its `start` position pointing to the beginning of the node in the source code, not the end. This is breaking source mapping and making it impossible to accurately trace back to the original source locations.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
