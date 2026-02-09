# Bug Report

### Describe the bug

I'm experiencing issues with error handling in async middleware functions. When a middleware function returns a rejected Promise, the error callback is being invoked incorrectly, and in some cases errors are being thrown when they shouldn't be.

### Reproduction

```js
// Middleware that returns a rejected promise
const middleware = async () => {
  throw new Error('Async error');
};

// When wrapping this middleware, the error handling doesn't work as expected
// The error gets passed to the wrong callback handler
```

Also seeing weird behavior where errors are thrown even when a callback is properly defined. It seems like the logic for determining whether to throw vs. call the error callback got mixed up.

### Expected behavior

- Rejected promises from async middleware should call the error callback (second argument to `.then()`)
- Errors should only be thrown when no callback is expected, not when a callback has been called
- Error handling should work consistently for both sync and async middleware

### System Info
- Node version: 18.x
- Package: remark@15.0.1

---
Repository: /testbed
