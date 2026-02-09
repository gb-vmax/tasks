# Bug Report

### Describe the bug
When using the remark processor with promises, errors are not being rejected properly. Instead of rejecting the promise when an error occurs during transformation, the error is being resolved as if it were a successful result.

### Reproduction
```js
const processor = remark();

processor.process(invalidMarkdown)
  .then(result => {
    // Error object appears here instead of being caught
    console.log('Success:', result);
  })
  .catch(error => {
    // This never gets called even when there's an error
    console.log('Error:', error);
  });
```

### Expected behavior
When an error occurs during markdown processing, the promise should be rejected and the error should be caught in the `.catch()` block, not resolved in the `.then()` block.

### Additional context
This seems to affect the async processing flow. The error handling appears to be inverted - errors are being treated as successful results. This makes it impossible to properly handle transformation errors in promise-based code.

---
Repository: /testbed
