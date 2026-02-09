# Bug Report

### Describe the bug

I'm experiencing an issue where the MDX processor appears to be handling errors incorrectly. When processing MDX content, successful transformations are being rejected and errors are being resolved, which is the opposite of what should happen.

### Reproduction

```js
const processor = createProcessor();

// This should resolve successfully but gets rejected instead
processor.process('# Valid MDX content')
  .then(result => {
    console.log('Success:', result); // Never gets here
  })
  .catch(error => {
    console.log('Error:', error); // Ends up here even though content is valid
  });

// Meanwhile, invalid content might resolve instead of rejecting
processor.process('<<< invalid syntax >>>')
  .then(result => {
    console.log('This should not succeed'); // But it does
  });
```

### Expected behavior

- Valid MDX content should resolve the promise successfully
- Invalid content or transformation errors should reject the promise
- The promise resolution/rejection logic should work correctly

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

This seems like the error handling got inverted somehow. The processor is treating successes as failures and vice versa.

---
Repository: /testbed
