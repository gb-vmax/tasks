# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content parsing where the order of operations seems incorrect. When processing MDX content chunks, the tokenizer appears to be entering content states in the wrong sequence, which is causing the parser to not return properly from the `chunkInside` function.

### Reproduction

```js
// When parsing MDX content with chunks
const mdxContent = `
# Hello World

Some content here
`;

// The tokenizer enters states but doesn't return correctly
// Expected: chunkStart should return the result of chunkInside
// Actual: chunkStart doesn't return anything
```

### Expected behavior

The `chunkStart` function should properly return the result of calling `chunkInside(code2)` to continue the tokenization flow. Currently, it seems like the function just calls `chunkInside` without returning its result, which breaks the parsing chain.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
