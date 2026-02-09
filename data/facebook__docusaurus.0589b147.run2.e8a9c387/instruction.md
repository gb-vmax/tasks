# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX pipeline processing where middleware functions are being skipped during execution. It appears that the first middleware in the pipeline never gets called, and the processing starts from the second middleware instead.

### Reproduction

```js
const { trough } = require('@mdx-js/mdx');

const pipeline = trough()
  .use((value, next) => {
    console.log('First middleware');
    next(null, value + ' -> first');
  })
  .use((value, next) => {
    console.log('Second middleware');
    next(null, value + ' -> second');
  });

pipeline.run('input', (err, result) => {
  console.log('Result:', result);
});

// Expected output:
// First middleware
// Second middleware
// Result: input -> first -> second

// Actual output:
// Second middleware
// Result: input -> second
```

### Expected behavior

All middleware functions in the pipeline should be executed in order, starting from the first one. The first middleware should process the input before passing it to subsequent middleware.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node.js version: 18.x

---
Repository: /testbed
