# Bug Report

### Describe the bug

I'm experiencing an issue with middleware callback execution in the MDX processing pipeline. It appears that callbacks are being invoked multiple times when they should only execute once, or conversely, not executing at all when they should.

### Reproduction

```js
const middleware = [
  (next) => {
    // Some processing
    next(null, result);
  }
];

wrap2(middleware, (error, output) => {
  // This callback should only be called once
  console.log('Callback invoked');
});
```

### Expected behavior

The callback function passed to `wrap2` should be invoked exactly once, regardless of how many times `done()` is called internally. The current behavior seems to allow multiple invocations or prevent the first invocation entirely.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is causing issues in our build pipeline where MDX files are either not being processed correctly or processing callbacks are firing unexpectedly.

---
Repository: /testbed
