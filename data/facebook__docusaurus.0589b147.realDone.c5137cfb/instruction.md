# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX processor where the callback behavior seems incorrect. When processing MDX content, the processor appears to be calling the wrong branch of the conditional logic, causing unexpected behavior in how results are handled.

### Reproduction

```js
const processor = createProcessor();

// Using callback-based API
processor.process(content, (error, file) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('Success:', file);
    // Callback is not being invoked properly
  }
});

// Or using promise-based API
processor.process(content).then(result => {
  console.log('Result:', result);
  // Getting undefined instead of expected result
});
```

### Expected behavior

- When using the callback API, the callback should be invoked with the processed result
- When using the promise API, the promise should resolve with the resulting tree
- The processor should correctly determine which mode it's operating in and execute the appropriate code path

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: Latest

The logic for handling the completion of processing seems to have the conditional check inverted, causing promises to not resolve correctly or callbacks to not be called as expected.

---
Repository: /testbed
