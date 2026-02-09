# Bug Report

### Describe the bug

I'm experiencing a critical issue after a recent update where MDX parsing completely breaks. The application crashes when trying to process any MDX content with what appears to be a syntax error in the vendored `@mdx-js/mdx` library.

### Reproduction

```js
// Any attempt to parse MDX content fails
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a simple MDX document.
`

// This throws an error
const result = await compile(mdxContent)
```

### Expected behavior

MDX content should be parsed and compiled successfully without errors. Line endings in the markdown should be handled properly by the tokenizer.

### Additional context

The error seems to be related to line ending tokenization in the micromark parser. It looks like there might be some corruption or accidental changes in the vendored dependency file at `jest/vendor/@mdx-js__mdx@3.0.0.js`.

The application was working fine before, and this started happening suddenly. I haven't made any changes to my MDX files or configuration.

---
Repository: /testbed
