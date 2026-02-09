# Bug Report

### Describe the bug

After a recent update, I'm experiencing an infinite recursion issue when using the MDX compiler. The build process hangs and eventually crashes with a "Maximum call stack size exceeded" error.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxSource = `
# Hello World

This is a simple MDX document.
`

// This causes infinite recursion
const result = await compile(mdxSource)
```

### Expected behavior

The MDX source should compile successfully without any recursion errors. The compiler should process the document and return the compiled output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening after the latest update. Previous versions worked fine with the same code.

---
Repository: /testbed
