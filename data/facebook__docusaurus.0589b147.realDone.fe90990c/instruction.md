# Bug Report

### Describe the bug

I'm experiencing an issue where error handling seems to be inverted when processing files. When there's an error during transformation, the promise resolves successfully instead of rejecting, and when processing completes without errors, the promise rejects.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkMdx);

// This should reject but resolves instead
processor.process('invalid content that causes an error')
  .then(result => {
    console.log('Success:', result); // This shouldn't happen
  })
  .catch(error => {
    console.log('Error:', error); // Expected to catch error here
  });

// This should resolve but rejects instead
processor.process('# Valid MDX content')
  .then(result => {
    console.log('Success:', result); // Expected to get result here
  })
  .catch(error => {
    console.log('Error:', error); // This shouldn't happen
  });
```

### Expected behavior

- When processing succeeds, the promise should resolve with the result
- When processing fails with an error, the promise should reject with the error

Currently it appears to be doing the opposite - rejecting on success and resolving on error.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
