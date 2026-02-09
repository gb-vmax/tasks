# Bug Report

### Describe the bug

I'm encountering an issue with the MDX processor where errors during transformation are not being properly rejected. Instead of the promise rejecting with the error, it seems to be resolving with the error object itself.

### Reproduction

```js
const processor = createProcessor();

try {
  const result = await processor.process(invalidMdxContent);
  // Expected: this code should not be reached
  // Actual: result contains an error object instead of throwing
  console.log(result); // Error object instead of processed content
} catch (error) {
  // Expected: error should be caught here
  // Actual: this block is never reached
  console.error('Caught error:', error);
}
```

### Expected behavior

When the MDX processor encounters an error during transformation, the promise should be rejected and the error should be catchable in a try/catch block or `.catch()` handler. The promise should not resolve with the error object.

### Additional context

This seems to affect error handling in the transformation pipeline. Errors that should be propagated properly are instead being treated as successful results, making it impossible to distinguish between successful processing and failures.

---
Repository: /testbed
