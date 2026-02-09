# Bug Report

### Describe the bug

I'm experiencing an issue where the MDX processor seems to be calling the wrong callback path when processing files. The processor appears to be resolving promises when it should be calling the callback function, and vice versa.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkMdx);

// Using callback-style API
processor.process(file, (error, result) => {
  // Callback never gets called with the result
  // Instead, it seems like the promise path is being taken
  console.log('This should print but doesn\'t');
});
```

### Expected behavior

When using the callback-style API (passing a `done` callback), the processor should invoke the callback with the result. When using the promise-style API (no callback), it should resolve the promise. Currently, the behavior seems inverted.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is causing issues in our build pipeline where we rely on the callback-based API for processing MDX files. The processor seems to hang or not properly complete the transformation.

---
Repository: /testbed
