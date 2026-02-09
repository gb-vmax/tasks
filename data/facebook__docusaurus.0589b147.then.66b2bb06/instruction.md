# Bug Report

### Describe the bug

I'm experiencing an issue where callback functions are being invoked multiple times with incorrect argument order. After recent changes, it appears that success callbacks are being called twice - once with swapped arguments and once with correct arguments.

### Reproduction

```js
const middleware = createMiddleware();

middleware.use((file, next) => {
  // Process file
  next();
});

middleware.run(file, (error, result) => {
  // This callback is being called multiple times
  // First call: (result, null) - wrong order
  // Second call: (null, result) - correct order
  console.log('Callback invoked with:', error, result);
});
```

### Expected behavior

The callback should only be invoked once with the correct argument order: `(error, result)` where `error` is null on success and `result` contains the processed value.

### Additional context

This seems to be affecting the middleware wrapper function. The double invocation causes unexpected behavior in async operations and can lead to race conditions when the same callback logic runs twice.

---
Repository: /testbed
