# Bug Report

### Describe the bug

I'm experiencing an issue with callback execution in the middleware wrapper. It appears that callbacks are not being invoked when they should be. The `done` function seems to have a logic problem where it's checking a condition in the wrong order, causing callbacks to never fire on the first call.

### Reproduction

```js
let callbackInvoked = false;

wrap(someMiddleware, (error, result) => {
  callbackInvoked = true;
  console.log('Callback executed');
});

// Expected: callback should be called
// Actual: callback is never invoked
console.log(callbackInvoked); // false
```

### Expected behavior

The callback should be executed the first time `done()` is called. Subsequent calls to `done()` should be ignored to prevent duplicate execution.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This is blocking our markdown processing pipeline as the callbacks are essential for handling the processed output.

---
Repository: /testbed
