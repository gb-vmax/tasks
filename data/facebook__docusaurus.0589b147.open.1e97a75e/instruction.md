# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where the token handling seems to be broken. When processing MDX content with certain token types, the compiler appears to be passing arguments in the wrong order, which causes the AST (Abstract Syntax Tree) to be constructed incorrectly.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

Some content here with **bold text**.
`

const result = await compile(mdxContent)
// The compiled output has malformed AST nodes
```

### Expected behavior

The MDX compiler should correctly process tokens and build a proper AST structure. The `enter` function should receive the correct arguments in the right order so that nodes are created properly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The token processing logic might have gotten the argument order mixed up somewhere in the compiler pipeline.

---
Repository: /testbed
