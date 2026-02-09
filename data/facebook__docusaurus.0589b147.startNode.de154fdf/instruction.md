# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where node positions are being tracked incorrectly. When parsing MDX content, the AST nodes seem to have wrong position information, which causes problems with source mapping and error reporting.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

Some text here
`

const result = await compile(mdxContent)

// The resulting AST nodes have incorrect position data
// Expected: nodes should have correct start positions
// Actual: nodes are initialized with wrong position parameters
```

### Expected behavior

AST nodes should be initialized with the correct start position (`this.start`) and start location (`this.startLoc`). Currently, it appears that position tracking is mixing up the parameters, leading to incorrect source mappings.

This affects:
- Error messages showing wrong line numbers
- Source map generation
- Any tooling that relies on accurate position information

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
