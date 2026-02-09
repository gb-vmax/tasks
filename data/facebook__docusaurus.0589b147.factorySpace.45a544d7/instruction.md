# Bug Report

### Describe the bug

I'm experiencing an issue with parsing markdown content that contains spaces. It seems like the space handling logic is inverted - spaces are being processed when they shouldn't be, and vice versa.

### Reproduction

When I try to parse markdown with specific whitespace patterns, the parser behaves unexpectedly:

```js
// Example markdown with spaces
const markdown = `
Some text with    multiple spaces
And another line
`;

// The parser doesn't handle the spaces correctly
const result = parse(markdown);
// Expected structure is malformed
```

The issue appears to be related to how the parser enters and exits space-related tokens. It's like the condition for detecting spaces got flipped somehow.

### Expected behavior

The parser should correctly identify and handle markdown spaces, entering the space token type when a space character is encountered and properly tracking the number of spaces consumed up to the limit.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

Has anyone else run into this? It's breaking markdown parsing for documents with whitespace.

---
Repository: /testbed
