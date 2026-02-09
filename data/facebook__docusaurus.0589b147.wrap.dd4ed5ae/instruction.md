# Bug Report

### Describe the bug

I'm experiencing an issue with the remark middleware wrapper where callbacks are being invoked multiple times or not at all in certain edge cases. The behavior seems inconsistent - sometimes the callback fires twice, and in other scenarios it doesn't fire when it should.

### Reproduction

```js
const middleware = (node, file, next) => {
  // Async operation
  setTimeout(() => {
    next();
  }, 100);
};

const wrapped = wrap(middleware, (error, result) => {
  console.log('Callback invoked');
  // This gets called multiple times unexpectedly
});

wrapped(node, file);
```

### Expected behavior

The callback should be invoked exactly once after the middleware completes, regardless of whether the middleware is synchronous or asynchronous. Currently seeing situations where:
1. The callback fires multiple times for the same operation
2. Errors aren't properly propagated when they should be

### System Info
- remark version: 15.0.1
- Node version: 18.x

This is causing issues in our processing pipeline where documents are being processed multiple times or error handling is not working as expected.

---
Repository: /testbed
