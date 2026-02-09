# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where the document structure isn't being properly closed/finalized. It seems like certain exit handlers are not being called during the compilation process, which leads to incomplete or malformed output.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test document with **bold** text.
`

const result = await compile(mdxContent)
// The compiled output is missing proper closing tags/structure
```

### Expected behavior

The MDX compiler should properly close all opened elements and call all necessary exit handlers to ensure the output is well-formed. All tokens should be properly processed through their complete lifecycle including exit callbacks.

### Additional context

This appears to affect documents with nested elements. The compilation completes without errors but the resulting structure is incomplete. It's like some cleanup step is being skipped.

---
Repository: /testbed
