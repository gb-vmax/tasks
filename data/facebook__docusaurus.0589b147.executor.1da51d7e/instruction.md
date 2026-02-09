# Bug Report

### Describe the bug

I'm encountering an issue with the remark processor where it seems to be executing the compilation step even when there are errors during the parse/run phase. The processor should stop and return the error, but instead it continues processing and tries to compile the tree, which can lead to unexpected behavior or crashes when the tree is malformed.

### Reproduction

```js
const remark = require('remark');

// Create a processor with a plugin that throws an error during run
const processor = remark().use(() => {
  return (tree, file, next) => {
    // Simulate an error during processing
    next(new Error('Processing failed'));
  };
});

// Try to process some markdown
processor.process('# Hello World', (err, file) => {
  console.log('Error:', err);
  console.log('File:', file);
});
```

### Expected behavior

When an error occurs during the `run` phase, the processor should:
1. Stop execution immediately
2. Call the callback/reject the promise with the error
3. NOT attempt to compile the (potentially invalid) tree

### Actual behavior

The processor continues to execute the compilation step even after an error is encountered, which can cause:
- Attempts to stringify invalid/undefined trees
- Cascading errors that mask the original error
- Unexpected behavior in the final output

This seems like a regression in error handling logic. The condition that checks for errors appears to be inverted - it's only returning early when there's NO error, instead of returning early when there IS an error.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
