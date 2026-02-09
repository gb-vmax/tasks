# Bug Report

### Describe the bug

I'm experiencing an issue with middleware chaining where the final callback is being invoked before all middleware functions have completed execution. This causes the callback to be called prematurely with incomplete or intermediate results, and then middleware continues to run after the callback has already been triggered.

### Reproduction

```js
const pipeline = trough()
  .use((value, next) => {
    // First middleware
    next(null, value + 1)
  })
  .use((value, next) => {
    // Second middleware
    next(null, value + 1)
  })

pipeline.run(0, (err, result) => {
  console.log('Callback called with:', result)
  // Expected: 2
  // Actual: callback fires too early
})
```

### Expected behavior

The final callback should only be invoked after all middleware in the chain has completed processing. Middleware should execute in sequence, and the callback should receive the final transformed value only when the entire pipeline is done.

### Additional context

This appears to affect any pipeline with multiple middleware functions. The callback gets triggered at the wrong time in the execution flow, which breaks the expected sequential processing behavior.

---
Repository: /testbed
