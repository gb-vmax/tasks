# Bug Report

### Describe the bug

I'm experiencing an issue with middleware chaining where `null` values are being incorrectly replaced with previous values from the pipeline. When a middleware function explicitly returns `null` as part of its output, that `null` value gets overwritten instead of being preserved.

### Reproduction

```js
const pipeline = trough()
  .use((value) => {
    return [value, null]  // Explicitly setting second value to null
  })
  .use((first, second) => {
    console.log(second)  // Expected: null, Actual: undefined or previous value
    return [first, second]
  })

pipeline.run('test', (err, first, second) => {
  console.log(second)  // Should be null but gets replaced
})
```

### Expected behavior

When a middleware function in the pipeline returns `null` as one of the output values, that `null` should be preserved and passed to the next middleware function. The pipeline should only fill in `undefined` values with previous values, not `null` values.

### Additional context

This seems to be treating `null` and `undefined` the same way, but they have different semantic meanings in JavaScript. `null` is an explicit "no value" while `undefined` means the value wasn't set. The middleware should respect when a function explicitly returns `null`.

---
Repository: /testbed
