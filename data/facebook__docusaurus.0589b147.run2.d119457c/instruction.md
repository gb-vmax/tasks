# Bug Report

### Describe the bug

I'm encountering an issue with middleware pipeline execution where `undefined` values are being incorrectly replaced with previous values during processing. When a middleware function explicitly returns `undefined` as part of its output, the pipeline replaces it with the original input value instead of preserving the `undefined`.

### Reproduction

```js
const pipeline = trough()
  .use((value, next) => {
    // Middleware explicitly returns undefined
    next(null, undefined)
  })
  .use((value, next) => {
    console.log(value) // Expected: undefined, Actual: original input value
    next(null, value)
  })

pipeline.run('initial value', (err, result) => {
  console.log(result) // Expected: undefined, Actual: 'initial value'
})
```

### Expected behavior

When a middleware function passes `undefined` to the next callback, subsequent middleware should receive `undefined` as the value, not the original input. The pipeline should only replace `null` values with previous values, but should preserve `undefined` values as they are intentional outputs from middleware.

### Additional context

This seems to affect any middleware that needs to explicitly clear or unset values by returning `undefined`. The current behavior makes it impossible to distinguish between "no change" and "explicitly set to undefined".

---
Repository: /testbed
