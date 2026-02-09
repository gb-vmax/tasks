# Bug Report

### Describe the bug

Getting a runtime error when using the MDX compiler. It seems like the `document` export from the constructs module is causing issues. The application crashes with an error about calling a non-function or trying to access properties on undefined.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test document.
`

// This throws an error
const result = await compile(mdxContent)
```

### Expected behavior

The MDX content should compile successfully without throwing errors. The `document` construct should be properly exported and usable by the compiler.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

The error started appearing recently and seems related to how the document construct is being exported. It's blocking our ability to compile any MDX files.

---
Repository: /testbed
