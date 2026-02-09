# Bug Report

### Describe the bug

I'm encountering an issue with the middleware pipeline execution in the `trough` function. It appears that the first middleware in the pipeline is being skipped entirely when `run()` is called.

### Reproduction

```js
const pipeline = trough()
  .use((value, next) => {
    console.log('First middleware:', value)
    next(null, value + 1)
  })
  .use((value, next) => {
    console.log('Second middleware:', value)
    next(null, value + 1)
  })

pipeline.run(10, (error, result) => {
  console.log('Final result:', result)
})
```

### Expected behavior

The output should be:
```
First middleware: 10
Second middleware: 11
Final result: 12
```

### Actual behavior

The first middleware is skipped and execution starts from the second middleware:
```
Second middleware: 10
Final result: 11
```

This seems to have started happening recently. The pipeline should execute all middleware functions in order, but the first one is never being called.

---
Repository: /testbed
