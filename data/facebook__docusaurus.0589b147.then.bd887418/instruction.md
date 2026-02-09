# Bug Report

### Describe the bug

I'm encountering an issue with the MDX compiler where processing appears to fail silently or produce incorrect results. The compilation seems to complete but the output is not what's expected, and in some cases errors are being passed where they shouldn't be.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test document.
`

const result = await compile(mdxContent)
// Expected: successful compilation
// Actual: unexpected behavior or error handling issues
```

When compiling valid MDX content, the process doesn't complete as expected. It seems like there might be an issue with how values are being passed through the compilation pipeline.

### Expected behavior

Valid MDX content should compile successfully without any issues. The compiler should properly handle the transformation and return the expected output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
