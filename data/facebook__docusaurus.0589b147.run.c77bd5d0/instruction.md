# Bug Report

### Describe the bug

When using the MDX processor's `run()` method with promises, errors are being resolved instead of rejected, and successful results are being rejected instead of resolved. This causes promise chains to behave completely backwards.

### Reproduction

```js
import {compile} from '@mdx-js/mdx'

const processor = compile('# Hello')

// This should reject but resolves with the error
processor.run(tree).catch(err => {
  console.log('Caught error:', err) // Never called
}).then(result => {
  console.log('Got result:', result) // This is actually an error object!
})

// Successful transformations also behave incorrectly
processor.run(validTree).then(result => {
  console.log('Success:', result) // Never called
}).catch(err => {
  console.log('Error:', err) // This is actually the successful tree!
})
```

### Expected behavior

- When an error occurs during transformation, the promise should be **rejected** with the error
- When transformation succeeds, the promise should be **resolved** with the resulting tree
- Error handlers (`.catch()`) should receive errors
- Success handlers (`.then()`) should receive the transformed tree

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This makes it impossible to properly handle errors when using the async/promise-based API. The callback-based API might still work correctly, but the promise API is completely broken.

---
Repository: /testbed
