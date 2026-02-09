# Bug Report

### Describe the bug

I'm encountering an issue with MDX comment handling where pragma comments are not being properly detected and removed from the output. It seems like the wrong comment index is being checked, causing the pragma comment to remain in the compiled output when it should be stripped out.

### Reproduction

```js
// Create an MDX file with a pragma comment
const mdxContent = `
/* @jsxRuntime classic */
# Hello World

Some content here
`;

// Compile with outputFormat: 'function-body'
const result = await compile(mdxContent, {
  outputFormat: 'function-body'
});

// The pragma comment is still present in the output
// when it should have been removed
```

### Expected behavior

The pragma comment (`/* @jsxRuntime classic */`) should be automatically removed from the compiled output when detected. The comment array should be properly checked at the correct index to identify and strip pragma comments.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to be checking the wrong position in the comments array, causing pragma comments to not be recognized and removed as intended.

---
Repository: /testbed
