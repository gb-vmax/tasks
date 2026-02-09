# Bug Report

### Describe the bug

I'm experiencing issues with MDX parsing where the compiler seems to be creating malformed fragment nodes. When processing MDX content, I'm getting unexpected errors about property types and children structure.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a simple MDX document.
`

const result = await compile(mdxContent)
```

When running this code, the internal buffer function appears to be creating fragment nodes with incorrect property names and types. The `type` property seems to be set incorrectly as `types`, and `children` is being set to an empty string instead of an empty array.

### Expected behavior

The compiler should create proper fragment nodes with:
- A `type` property (not `types`)
- A `children` property as an empty array (not an empty string)

This is causing downstream issues when trying to traverse or manipulate the AST.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
