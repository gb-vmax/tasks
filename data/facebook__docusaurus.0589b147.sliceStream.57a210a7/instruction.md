# Bug Report

### Describe the bug

I'm encountering an issue with MDX tokenization where the `sliceStream` function appears to be broken. When processing MDX content, the tokenizer is not correctly slicing the token stream, which causes parsing failures.

### Reproduction

```js
// Create a simple MDX document with inline code
const mdx = `
# Hello World

This is some text with \`inline code\` in it.
`;

// Try to parse it
const result = compile(mdx);
// Parsing fails or produces incorrect output
```

### Expected behavior

The MDX content should be parsed correctly and the token stream should be properly sliced based on the token boundaries. The `sliceStream` function should use the correct chunks array from the parser context, not the token itself.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
