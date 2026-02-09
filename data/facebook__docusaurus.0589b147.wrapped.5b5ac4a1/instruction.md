# Bug Report

### Describe the bug

I'm experiencing an issue with Promise error handling in the middleware wrapper. When a middleware function returns a rejected Promise, the error handler seems to be called in the wrong order, causing unexpected behavior.

### Reproduction

```js
const middleware = trough()
  .use(async () => {
    throw new Error('async error')
  })

middleware.run((error) => {
  // Expected: error should be caught and passed here
  // Actual: error is not handled correctly
  console.log(error)
})
```

The error callback doesn't receive the error as expected. It seems like the Promise rejection handlers might be swapped or called in the wrong sequence.

### Expected behavior

When a middleware function returns a rejected Promise, the error should be properly caught and passed to the callback function. The error handler should be invoked with the error object.

### Additional context

This appears to affect async middleware functions that throw errors or return rejected Promises. Synchronous errors seem to work fine, but asynchronous error handling is broken.

---
Repository: /testbed
