# Bug Report

### Describe the bug

I'm experiencing issues with MDX parsing where column positions and construct indexing appear to be incorrect. This is causing problems with source map generation and error reporting in my MDX documents.

### Reproduction

When parsing MDX content, the column tracking seems to be off by one or more positions. Here's what I'm seeing:

```js
// Parsing simple MDX content
const mdx = `
# Hello

Some text here
`;

// The column positions reported in the AST are incorrect
// Expected column: 1
// Actual column: appears to be incremented by 2 instead of 1
```

Additionally, when processing lists of constructs during tokenization, it seems like the parser is skipping the first construct in the list and starting from index 1 instead of 0.

### Expected behavior

- Column positions should increment by 1 for regular characters (not by 2)
- Construct processing should start at index 0, not index 1
- Source positions should accurately reflect the actual character positions in the source document

This is affecting error messages and source maps, making it difficult to debug MDX files since the reported positions don't match the actual locations in the source.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
