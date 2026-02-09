# Bug Report

### Describe the bug

I'm experiencing an issue where middleware callbacks are being invoked multiple times instead of just once. This is causing duplicate processing and unexpected behavior in my application.

### Reproduction

```js
const middleware = wrap(myMiddleware, (error, result) => {
  console.log('Callback invoked');
  // This gets called multiple times
});

// After processing, the callback fires more than once
```

The callback should only execute once, but it seems like the guard condition isn't working properly and allows multiple invocations.

### Expected behavior

The callback should only be called once, even if `done()` is called multiple times. Subsequent calls should be ignored.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
