# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the parser seems to be returning incorrect values. When trying to parse MDX content, I'm getting unexpected behavior - it looks like the parser is either not processing events correctly or returning the wrong result type.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test MDX document.
`

const result = await compile(mdxContent)
// Expected: compiled MDX output
// Actual: unexpected result or error
```

### Expected behavior

The parser should properly process the MDX content and return the compiled output. The postprocessing step should iterate through events correctly and return the processed events array.

### Additional context

This seems to be related to the internal event processing logic. The parser appears to be stuck in an infinite loop or returning an incorrect value type instead of the expected events array.

---
Repository: /testbed
