# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where the context (`this`) is being lost during token processing. The compiler seems to be calling methods with incorrect context binding, which causes the enter/exit flow to fail silently or produce unexpected results.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a paragraph with **bold text**.
`

const result = await compile(mdxContent)
```

When processing tokens during compilation, the opener function appears to be calling methods with the wrong context. This affects how tokens are entered into the stack and can lead to malformed AST structures or runtime errors when the compiled MDX is used.

### Expected behavior

The compiler should maintain proper context (`this`) when calling token processing methods. The enter/exit flow should work correctly with the proper object context throughout the compilation process.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
