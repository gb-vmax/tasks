# Bug Report

### Describe the bug

I'm experiencing an issue with middleware execution in the trough pipeline. When chaining multiple middleware functions, the pipeline seems to skip the first middleware function and starts execution from the second one instead.

### Reproduction

```js
const pipeline = trough()
  .use((value) => {
    console.log('First middleware:', value);
    return value + 1;
  })
  .use((value) => {
    console.log('Second middleware:', value);
    return value + 1;
  })
  .use((value) => {
    console.log('Third middleware:', value);
    return value + 1;
  });

pipeline.run(0, (err, result) => {
  console.log('Final result:', result);
});

// Expected output:
// First middleware: 0
// Second middleware: 1
// Third middleware: 2
// Final result: 3

// Actual output:
// Second middleware: 0
// Third middleware: 1
// Final result: 2
```

The first middleware in the chain is never called, and the entire pipeline behaves as if it starts from index 1 instead of 0.

### Expected behavior

All middleware functions should be executed in order, starting from the first one added to the pipeline.

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
