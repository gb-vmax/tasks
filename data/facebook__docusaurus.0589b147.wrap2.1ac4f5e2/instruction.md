# Bug Report

### Describe the bug

I'm experiencing issues with MDX processing where middleware callbacks are being invoked incorrectly. It appears that the callback handling logic has been inverted, causing callbacks to be called multiple times or not at all depending on the middleware signature.

### Reproduction

```js
// When using middleware that expects a callback parameter
const middleware = (context, next) => {
  // Process something
  next();
};

// The callback gets added to parameters when it shouldn't
// This causes the middleware to receive unexpected arguments
```

Alternatively:

```js
// When using middleware that doesn't expect a callback
const middleware = (context) => {
  // Process synchronously
  return result;
};

// The callback doesn't get added when it should
// This breaks the async flow
```

### Expected behavior

- Middleware functions that expect a callback (arity > parameters.length) should receive the callback as an additional parameter
- Middleware functions that don't expect a callback should work synchronously without the callback being added
- The done callback should only be called once to prevent duplicate invocations

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have broken the middleware wrapper functionality. Any async middleware or plugins that rely on callback-based flow control are affected.

---
Repository: /testbed
