# Bug Report

### Describe the bug

I'm experiencing an issue with the middleware pipeline execution in the trough function. When running a pipeline with multiple middleware functions, the first middleware is being skipped and execution starts from the second one instead.

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

pipeline.run(0, (err, result) => {
  console.log('Final result:', result)
})
```

Expected output:
```
First middleware: 0
Second middleware: 1
Final result: 2
```

Actual output:
```
Second middleware: 0
Final result: 1
```

The first middleware function is never executed, causing the pipeline to start from the second middleware instead.

### Expected behavior

All middleware functions should be executed in order, starting from the first one added to the pipeline.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: 18.x

---
Repository: /testbed
