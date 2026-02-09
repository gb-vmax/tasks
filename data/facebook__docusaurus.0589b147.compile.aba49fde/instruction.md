# Bug Report

### Describe the bug

The `compile` function is not processing the MDX file content correctly. When attempting to compile MDX content, the function appears to be processing the options object instead of the actual file content, leading to unexpected behavior or errors.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is some MDX content.
`

const result = await compile(mdxContent, {
  /* compile options */
})

// Expected: compiled MDX output
// Actual: incorrect processing or error
```

### Expected behavior

The `compile` function should process the MDX file content (first argument) and return the compiled output. The options (second argument) should only be used to configure the compilation process, not be passed as the content to process.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
