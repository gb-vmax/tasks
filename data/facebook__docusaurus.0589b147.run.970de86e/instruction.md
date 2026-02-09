# Bug Report

### Describe the bug

When using the `run()` method with a callback function, errors are not being handled correctly. If an error occurs during transformation and a callback is provided, the promise gets resolved instead of the callback being invoked with the error.

### Reproduction

```js
const processor = remark();

// Using callback style
processor.run(tree, (error, result) => {
  if (error) {
    console.log('Error handled:', error);
  } else {
    console.log('Success:', result);
  }
});

// When an error occurs during transformation, the callback is never 
// called with the error parameter
```

### Expected behavior

When using the callback-style API with `run()`, if an error occurs during transformation, the callback should be invoked with the error as the first argument. Currently it seems like the error handling logic is mixing up the callback and promise-based approaches.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
