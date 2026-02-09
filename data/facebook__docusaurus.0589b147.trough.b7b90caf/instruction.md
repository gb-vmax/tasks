# Bug Report

### Describe the bug

I'm experiencing an issue with middleware execution in the trough pipeline. When chaining multiple middleware functions, the pipeline appears to skip the first middleware function and starts execution from the second one instead.

### Reproduction

```js
const pipeline = trough()
  .use((value) => {
    console.log('First middleware:', value)
    return value + 1
  })
  .use((value) => {
    console.log('Second middleware:', value)
    return value + 1
  })
  .use((value) => {
    console.log('Third middleware:', value)
    return value + 1
  })

pipeline.run(0, (err, result) => {
  console.log('Final result:', result)
})
```

Expected output:
```
First middleware: 0
Second middleware: 1
Third middleware: 2
Final result: 3
```

Actual output:
```
Second middleware: 0
Third middleware: 1
Final result: 2
```

The first middleware is never executed, and the entire chain is off by one.

### Expected behavior

All middleware functions should execute in order, starting from the first one added to the pipeline.

### Additional context

This appears to have started happening recently. The middleware counter seems to be incrementing at the wrong time, causing the pipeline to skip the initial function.

---
Repository: /testbed
