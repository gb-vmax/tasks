# Bug Report

### MDX compiler crashes when processing certain token types

I've encountered an issue with the MDX compiler where it throws an error when processing specific markdown/JSX constructs. The compiler seems to be failing during the token opening phase.

### Reproduction
```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello

<CustomComponent>
  Some content here
</CustomComponent>
`

// Compiler throws an error during processing
await compile(mdxContent)
```

### Expected behavior
The MDX content should compile successfully without errors. The compiler should handle opening tokens properly regardless of whether additional processing callbacks are defined.

### Actual behavior
Getting a runtime error when the compiler tries to process opening tokens. It appears to be calling a function that doesn't exist in certain cases.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. Any help would be appreciated!

---
Repository: /testbed
