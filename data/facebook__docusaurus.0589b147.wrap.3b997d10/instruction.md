# Bug Report

### Describe the bug

I'm experiencing an issue with middleware callback handling in remark. When using middleware functions with callbacks, the execution flow seems broken - callbacks are either not being called properly or errors are being thrown unexpectedly.

### Reproduction

```js
const middleware = (node, file, next) => {
  // Do some async processing
  setTimeout(() => {
    next();
  }, 100);
};

// When this middleware is wrapped and executed, 
// it throws errors or doesn't call the callback correctly
```

### Expected behavior

Middleware functions that expect callbacks should:
1. Execute the callback when provided
2. Handle async operations correctly
3. Not throw errors when callbacks are properly invoked

The middleware wrapper should distinguish between callback-based and promise-based middleware and handle each appropriately.

### System Info
- remark version: 15.0.1
- Node.js version: Latest LTS

---
Repository: /testbed
