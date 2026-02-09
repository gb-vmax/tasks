# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content parsing where the order of operations during tokenization appears to be causing problems with text chunk processing. The text content isn't being properly linked in the token chain, which leads to incorrect parsing results.

### Reproduction

```js
const mdx = `
Some text content
with line breaks
and multiple lines
`;

// Parse the MDX content
const result = compile(mdx);
// The resulting token chain has incorrect linkage between text chunks
```

When processing markdown content with line endings, the token chain gets corrupted because tokens are being linked before they're fully initialized. This causes the `previous` token reference to point to the wrong token in the sequence.

### Expected behavior

Text chunks should be properly connected in the token chain with correct `next` and `previous` references. Each token should be fully set up before being linked to the previous token.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
