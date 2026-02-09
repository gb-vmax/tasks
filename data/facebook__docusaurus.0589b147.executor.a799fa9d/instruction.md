# Bug Report

### Describe the bug

When using the processor with a callback function and an error occurs during transformation, the error is not being properly propagated to the callback. Instead of calling the callback with the error, the processor appears to be swallowing it or handling it incorrectly.

### Reproduction

```js
const processor = remark();

processor.process(tree, file, (error, result) => {
  if (error) {
    console.log('Error caught:', error);
  } else {
    console.log('Success:', result);
  }
});

// When a transformer throws an error, the callback is never invoked with the error
// Expected: callback should be called with error parameter
// Actual: error is not passed to the callback
```

### Expected behavior

When an error occurs during the transformation process and a callback is provided (instead of using promises), the callback should be invoked with the error as the first parameter according to the standard Node.js callback pattern.

### Additional context

This seems to affect the callback-based API specifically. When using promises, error handling might work differently, but the traditional callback pattern should still properly propagate errors to the done callback.

---
Repository: /testbed
