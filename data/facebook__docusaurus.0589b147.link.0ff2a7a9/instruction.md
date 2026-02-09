# Bug Report

### Describe the bug

I'm experiencing an issue with link rendering in MDX where the position information seems to be incorrect or missing. When processing links, the resulting element doesn't have the proper position data attached to it.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
[My Link](https://example.com)
`

const result = await compile(mdxContent)
// The link element's position data is not correctly set
```

When I inspect the generated AST, the link nodes don't have the expected position information that should be carried over from the original markdown node.

### Expected behavior

The link element should have position information properly transferred from the source markdown node. The position data should be available on the resulting HAST node for source mapping and debugging purposes.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
