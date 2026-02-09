# Bug Report

### Describe the bug

When processing files with the MDX processor, errors during the run phase are not being properly handled. The error callback receives the file object instead of the error, causing the error to be lost and potentially leading to undefined behavior or silent failures.

### Reproduction

```js
import {compile} from '@mdx-js/mdx'

// Create a processor that will encounter an error during run phase
const processor = compile(someInvalidMdxContent)

processor.process(file, (error, result) => {
  // error is undefined even when processing fails
  // result contains the file object instead
  console.log(error) // undefined
  console.log(result) // file object
})
```

### Expected behavior

When an error occurs during the run phase, the error callback should receive the actual error as the first parameter, not the file object. The callback signature should be `(error, file)` where error is defined when something goes wrong.

Currently it seems like errors are being swallowed and the file is passed where the error should be, making it impossible to properly handle processing failures.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
