# Bug Report

### Describe the bug

When processing markdown files with transformers that encounter errors, the callback-based API doesn't properly invoke the `done` callback with the error. The error is silently swallowed instead of being passed to the callback handler.

### Reproduction

```js
const processor = remark();

processor.process(someMarkdownContent, (error, file) => {
  if (error) {
    console.log('Error occurred:', error);
  } else {
    console.log('Success:', file);
  }
});
```

When a transformer throws an error during processing, the `done` callback is never called with the error parameter. The callback just doesn't fire at all in error cases.

### Expected behavior

The `done` callback should be invoked with the error as the first parameter when an error occurs during transformation, following standard Node.js callback conventions.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
