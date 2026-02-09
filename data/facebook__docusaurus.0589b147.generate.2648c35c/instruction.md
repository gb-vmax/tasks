# Bug Report

### Describe the bug

The MDX code generation is returning empty output when processing nodes. After generating the AST and calling the generate function, the returned string is completely empty instead of containing the expected JavaScript/JSX code.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test paragraph.
`

const result = await compile(mdxContent)
console.log(result.value) // Expected: generated code, Actual: empty string
```

### Expected behavior

The `generate()` function should return the compiled JavaScript/JSX code for the MDX content. The output should contain the transformed code that can be evaluated or used in a React application.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
