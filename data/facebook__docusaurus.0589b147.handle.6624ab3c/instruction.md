# Bug Report

### Describe the bug

I'm experiencing an issue where MDX content fails to render when processing certain node structures. The content just doesn't appear in the output, and there's no error message or warning to indicate what went wrong.

### Reproduction

```js
// When processing MDX with specific node patterns
const mdx = `
# Hello World

Some content here
`;

const result = await compile(mdx);
// Output is empty or missing expected content
```

### Expected behavior

The MDX content should be properly compiled and all nodes should be rendered in the output. Currently it seems like valid nodes are being skipped during the compilation process.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. Not sure if it's related to a recent change in how nodes are being handled internally.

---
Repository: /testbed
