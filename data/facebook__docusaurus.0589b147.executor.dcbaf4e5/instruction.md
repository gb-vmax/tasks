# Bug Report

### Describe the bug

I'm encountering an issue with the processor's error handling logic. When processing files, errors are being rejected even when the processing completes successfully, while successful results are being resolved when there's actually an error.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkRehype)
  .use(rehypeStringify);

// This should succeed but gets rejected
processor.process('# Hello World')
  .then(result => {
    console.log('Success:', result); // Never called
  })
  .catch(error => {
    console.log('Error:', error); // Called even though processing succeeded
  });

// This should fail but might get resolved
processor.process(null)
  .then(result => {
    console.log('Success:', result); // Might be called incorrectly
  })
  .catch(error => {
    console.log('Error:', error); // Should be called
  });
```

### Expected behavior

- Successful processing should resolve the promise with the result
- Errors during processing should reject the promise with the error
- The promise resolution logic should correctly distinguish between success and failure cases

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to be related to the conditional logic in the `realDone` callback function. The error and success paths appear to be inverted.

---
Repository: /testbed
