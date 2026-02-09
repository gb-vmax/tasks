# Bug Report

### Describe the bug

I'm encountering an issue with the MDX processor where errors during the run phase are not being handled correctly. When an error occurs but the tree and file are still present, the processor continues execution instead of stopping and reporting the error.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkMdx)
  .use(() => (tree, file) => {
    // Plugin that throws an error but doesn't clear tree/file
    throw new Error('Processing error');
  })
  .use(remarkRehype)
  .use(rehypeStringify);

// Process a file
processor.process('# Hello').then(
  (result) => {
    console.log('Success:', result); // This gets called unexpectedly
  },
  (error) => {
    console.log('Error:', error); // This should be called but isn't
  }
);
```

### Expected behavior

When an error occurs during processing, even if the tree and file objects are still present, the processor should reject the promise and pass the error to the error handler. Currently, it seems to ignore the error and continue with compilation when both tree and file exist.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
