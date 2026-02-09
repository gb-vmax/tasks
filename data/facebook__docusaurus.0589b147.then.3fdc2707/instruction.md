# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX processor where it seems to be hanging or not completing properly. When trying to process MDX content, the callback never gets called and the process just stalls indefinitely.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

This is a test document.
`

compile(mdxContent)
  .then(result => {
    console.log('Compilation successful:', result)
  })
  .catch(error => {
    console.error('Compilation failed:', error)
  })
```

### Expected behavior

The MDX content should compile successfully and the promise should resolve with the compiled result. The `then` callback should be invoked with the compilation output.

### Actual behavior

The promise never resolves. No output is produced and the callback is never called. The process appears to hang without any error messages.

This is blocking our documentation build pipeline. Any help would be appreciated!

### System Info
- @mdx-js/mdx version: 3.0.0
- Node.js version: 18.x

---
Repository: /testbed
