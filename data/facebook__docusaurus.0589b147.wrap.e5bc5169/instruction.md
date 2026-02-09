# Bug Report

### Describe the bug

I'm experiencing an issue with error handling in the middleware wrapper. When an exception occurs during middleware execution, the error callback is being invoked multiple times instead of just once. This leads to unexpected behavior where error handlers receive duplicate error notifications.

### Reproduction

```js
const middleware = (req, res, next) => {
  throw new Error('Test error');
};

const wrappedMiddleware = wrap(middleware, (error, result) => {
  console.log('Error callback invoked:', error);
  // This gets called multiple times with the same error
});

wrappedMiddleware();
```

### Expected behavior

The error callback should only be invoked once when an exception is thrown. Currently it appears the callback is being triggered multiple times for the same error, which can cause issues in error handling logic that assumes single invocation.

### Additional context

This seems to affect middleware that throws exceptions synchronously. The duplicate callbacks make it difficult to properly handle errors in application code since cleanup or logging logic may execute multiple times unintentionally.

---
Repository: /testbed
