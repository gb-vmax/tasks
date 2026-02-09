# Bug Report

### Describe the bug

I'm experiencing an issue with async middleware execution where Promise results are not being handled correctly. When a middleware function returns a Promise, the system seems to be treating it incorrectly, leading to unexpected behavior in the callback chain.

### Reproduction

```js
const middleware = trough()
  .use(async (value) => {
    // Async operation that returns a Promise
    return Promise.resolve(value + 1)
  })
  .use((value) => {
    console.log('Expected:', value + 1)
    console.log('Actual:', value)
  })

middleware.run(5, (err, result) => {
  // Callback is not invoked properly
  console.log('Final result:', result)
})
```

### Expected behavior

When a middleware function returns a Promise, it should be properly awaited and the resolved value should be passed to the next middleware in the chain. The final callback should receive the correct result after all middleware has executed.

### Additional context

This appears to affect middleware that:
- Returns Promise objects
- Has synchronous execution (no callback parameter)
- Needs to pass results through the chain

The issue seems to be related to how Promise results and Error objects are being differentiated and handled in the middleware wrapper logic.

---
Repository: /testbed
