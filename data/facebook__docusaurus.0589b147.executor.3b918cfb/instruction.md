# Bug Report

### Describe the bug

I'm encountering an issue with the MDX processor where errors during transformation are being handled incorrectly. When a transformer throws an error, it seems like the promise is being rejected with the wrong value, and the control flow logic appears inverted.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkMdx)
  // ... other plugins

processor.process('# Hello')
  .then(result => {
    console.log('Success:', result)
  })
  .catch(error => {
    // Expected to receive the actual error object here
    // but getting something else instead
    console.log('Error:', error)
  })
```

### Expected behavior

When an error occurs during processing:
- The promise should be rejected with the error object
- The error handler should receive the actual error, not the tree

When processing succeeds:
- The promise should be resolved with the resulting tree
- Success handlers should be called appropriately

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

The error handling seems backwards - successful transformations might not be resolving properly, and errors might be passing the wrong values to rejection handlers.

---
Repository: /testbed
