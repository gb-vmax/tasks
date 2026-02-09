# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where the output seems to be returning the wrong value during the markdown-to-JSX transformation. The compiled MDX content is not what I expect - it appears that instead of getting the converted string content, I'm getting something else entirely from the processing stack.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test paragraph with **bold text**.
`

const result = await compile(mdxContent)
console.log(result)
// Expected: Properly compiled JSX output
// Actual: Unexpected/incorrect output
```

### Expected behavior

The MDX compiler should return the properly converted string representation of the markdown content transformed into JSX. The compilation process should maintain the correct order of operations when processing the internal stack.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken recently and is affecting all MDX compilation in my project. Any help would be appreciated!

---
Repository: /testbed
