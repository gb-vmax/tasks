# Bug Report

### Describe the bug

I'm encountering an issue with async middleware error handling. When a middleware function returns a rejected Promise, the error is not being properly caught and propagated through the callback chain.

### Reproduction

```js
const middleware = async () => {
  throw new Error('Something went wrong');
};

wrap2(middleware, (err) => {
  // Expected: err should be the Error object
  // Actual: callback is never called with the error
  console.log('Error:', err);
});
```

The callback should be invoked with the error, but it seems like rejected promises aren't being handled correctly. This is causing errors to be silently swallowed instead of being passed to the error handler.

### Expected behavior

When a middleware function throws an error or returns a rejected Promise, the error should be passed to the callback function so it can be properly handled.

### Additional context

This appears to affect middleware functions that return promises. Synchronous errors seem to work fine, but async errors just disappear without triggering the callback.

---
Repository: /testbed
