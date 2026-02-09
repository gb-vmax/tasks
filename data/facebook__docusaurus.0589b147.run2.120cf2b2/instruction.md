# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX pipeline where middleware functions are being executed in the wrong order or not at all. It seems like the middleware chain is broken and functions aren't being called sequentially as expected.

### Reproduction

```js
const pipeline = trough();

pipeline
  .use((value, next) => {
    console.log('First middleware:', value);
    next(null, value + 1);
  })
  .use((value, next) => {
    console.log('Second middleware:', value);
    next(null, value + 1);
  })
  .use((value, next) => {
    console.log('Third middleware:', value);
    next(null, value + 1);
  });

pipeline.run(0, (err, result) => {
  console.log('Final result:', result);
});
```

### Expected behavior

The middleware should execute in order:
- First middleware: 0
- Second middleware: 1
- Third middleware: 2
- Final result: 3

### Actual behavior

The middleware chain doesn't execute properly. The first middleware seems to be skipped or the execution order is incorrect, leading to unexpected results or no output at all.

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to have started recently, possibly after a recent update to the trough pipeline implementation. The middleware execution flow seems broken.

---
Repository: /testbed
