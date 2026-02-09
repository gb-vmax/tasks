# Bug Report

### Describe the bug

I'm experiencing an issue with promise handling in middleware functions. When a middleware returns a rejected promise, the error handler is being called with the resolved value instead of the error, and vice versa.

### Reproduction

```js
const middleware = () => {
  return Promise.reject(new Error('Something went wrong'));
};

// The error is not being caught properly
// Instead of calling the error handler, it calls the success handler
wrap2(middleware, (err, result) => {
  if (err) {
    console.log('Error:', err); // This should be called but isn't
  } else {
    console.log('Success:', result); // This gets called incorrectly
  }
});
```

Similarly, when a promise resolves successfully:

```js
const middleware = () => {
  return Promise.resolve('success');
};

// The success value ends up in the error parameter
wrap2(middleware, (err, result) => {
  // err contains 'success' instead of result
});
```

### Expected behavior

When a middleware function returns a rejected promise, the error callback should receive the error. When it returns a resolved promise, the success callback should receive the result value.

The promise handlers seem to be swapped - rejection is treated as success and success is treated as an error.

---
Repository: /testbed
