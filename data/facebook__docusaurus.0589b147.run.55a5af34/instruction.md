# Bug Report

### Describe the bug

I'm encountering an issue with the remark pipeline error handling. When an error occurs during middleware execution, the error callback receives the wrong values - it gets the original input values instead of the intermediate output values that were being processed when the error occurred.

### Reproduction

```js
const processor = remark()
  .use(() => (tree, file, next) => {
    // Modify the tree/values
    const modifiedValue = { modified: true };
    next(null, modifiedValue);
  })
  .use(() => (tree, file, next) => {
    // This middleware throws an error
    next(new Error('Something went wrong'));
  });

processor.process(originalInput, (err, result) => {
  // Expected: err callback should receive the modified values
  // Actual: err callback receives the original input values
  console.log(result); // Shows original input instead of modified intermediate values
});
```

### Expected behavior

When an error occurs in the middleware pipeline, the error callback should receive the intermediate values that were being processed at the time of the error, not the original input values. This is important for debugging and understanding what state the data was in when the error occurred.

### System Info

- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
