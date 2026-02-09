# Bug Report

### Describe the bug

I'm experiencing an issue with node type checking in MDX processing. It seems like the type validation logic is inverted - nodes that should pass validation are being rejected, and nodes that should be rejected are passing through.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a paragraph with **bold text**.
`

const result = await compile(mdxContent)
// Expected: Successfully compiled MDX
// Actual: Type checking fails or produces incorrect results
```

When processing MDX content with various node types (headings, paragraphs, emphasis, etc.), the validation appears to be working backwards. Valid nodes are being filtered out while invalid ones pass through.

### Expected behavior

The type checking function should correctly identify and validate node types. Valid MDX nodes should pass validation checks, and invalid nodes should be rejected.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
