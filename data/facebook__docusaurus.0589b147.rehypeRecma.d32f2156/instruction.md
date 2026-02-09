# Bug Report

### Describe the bug

After a recent update, MDX compilation is failing with unexpected errors. The transformed output structure seems to have changed, causing the compiler to break when processing MDX files.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test MDX file.
`

const result = await compile(mdxContent)
// Compilation fails or produces incorrect output
```

### Expected behavior

The MDX content should compile successfully and return a valid JavaScript module that can be evaluated. The transformation pipeline should work as before without breaking changes to the output structure.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
