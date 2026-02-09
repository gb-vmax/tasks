# Bug Report

### Describe the bug

I'm encountering an issue with the middleware pipeline where it seems to stop processing when no arguments are passed through the chain. The pipeline appears to halt prematurely instead of continuing to execute all registered middleware functions.

### Reproduction

```js
const pipeline = trough()
  .use((next) => {
    console.log('Middleware 1')
    next()  // Calling next with no arguments
  })
  .use((next) => {
    console.log('Middleware 2')
    next()
  })

pipeline.run((err) => {
  console.log('Done')
})
```

**Expected output:**
```
Middleware 1
Middleware 2
Done
```

**Actual output:**
```
Middleware 1
Done
```

The second middleware never executes when the first middleware calls `next()` without any arguments.

### Expected behavior

The middleware pipeline should continue executing all registered middleware functions even when `next()` is called without arguments. Each middleware should be invoked in sequence until the chain is complete.

### Additional context

This seems to have started happening recently. Previously, the pipeline would correctly process all middleware regardless of whether arguments were passed through or not. Now it appears to short-circuit the execution when the values array is empty.

---
Repository: /testbed
