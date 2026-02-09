# Bug Report

### Describe the bug

I'm encountering an issue with error handling in the MDX processor. When processing fails with an error, the promise doesn't reject properly and instead seems to resolve with the file or call the done callback incorrectly.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

// Try to compile invalid MDX that will produce an error
compile('invalid MDX content that causes an error')
  .then(result => {
    console.log('Resolved:', result) // This shouldn't happen on error
  })
  .catch(error => {
    console.log('Rejected:', error) // Expected to reach here
  })
```

### Expected behavior

When the MDX compilation encounters an error, the promise should be rejected and the catch block should be executed. Currently, it seems like errors are not being handled correctly and the promise resolution logic is behaving unexpectedly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
