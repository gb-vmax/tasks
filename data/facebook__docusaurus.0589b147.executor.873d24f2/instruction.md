# Bug Report

### Describe the bug

MDX processing fails when using the `process()` method with valid input. The processor appears to be rejecting valid parse results and not continuing to the compilation step.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test MDX file.
`

// This should work but fails
const result = await compile(mdxContent)
console.log(result)
```

### Expected behavior

The MDX content should be processed successfully and return the compiled output. The processor should parse the content, run transformations, and compile it to the final result.

### Actual behavior

The processing stops prematurely and doesn't produce the expected output. It seems like valid parse results are being treated as errors and the compilation step is never reached.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
