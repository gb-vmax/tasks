# Bug Report

### Describe the bug

I'm experiencing an issue with middleware execution in the trough pipeline. It seems like the middleware functions are being skipped or executed in the wrong order, causing unexpected behavior in my MDX processing pipeline.

### Reproduction

```js
const pipeline = trough()
  .use(function(value, next) {
    console.log('First middleware:', value);
    next(null, value + 1);
  })
  .use(function(value, next) {
    console.log('Second middleware:', value);
    next(null, value + 1);
  })
  .use(function(value, next) {
    console.log('Third middleware:', value);
    next(null, value + 1);
  });

pipeline.run(0, function(err, result) {
  console.log('Final result:', result);
});
```

### Expected behavior

All middleware functions should execute in sequence, with each one receiving the output from the previous middleware. The first middleware should be called with the initial value.

### Actual behavior

The middleware execution appears to be skipping the first function or not properly passing values through the chain. The pipeline doesn't behave as expected when multiple middleware functions are chained together.

### System Info

- MDX version: 3.0.0
- Node version: 18.x

This is blocking my ability to use custom transformers in my MDX content pipeline. Any help would be appreciated!

---
Repository: /testbed
