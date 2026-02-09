# Bug Report

### Describe the bug

I'm experiencing an issue with middleware callback execution in the MDX processor. It appears that callbacks are being invoked multiple times or error handling is not working correctly, leading to unexpected behavior in the middleware chain.

### Reproduction

```js
// Setting up a middleware that expects a callback
const middleware = (next) => {
  // Perform some async operation
  setTimeout(() => {
    next(new Error('Something went wrong'));
  }, 100);
};

// When the error callback is triggered, the behavior is inconsistent
// Sometimes the error is thrown, sometimes it's passed to the callback
// Multiple invocations seem to occur
```

### Expected behavior

The middleware callback should only be invoked once, and errors should be handled consistently. When an error occurs in middleware, it should either be thrown OR passed to the callback, but the current behavior seems unpredictable.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
