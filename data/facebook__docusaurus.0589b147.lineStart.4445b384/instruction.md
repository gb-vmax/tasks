# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content parsing where linked list nodes seem to be incorrectly connected. When processing text chunks in paragraphs, the `next` property of previous tokens is being set to reference themselves instead of the newly created token.

### Reproduction

```js
// When parsing MDX content with multiple text chunks
const mdxContent = `
This is a paragraph with multiple
lines of text content.
`;

// The token chain gets corrupted because previous2.next 
// points to previous2 itself after it's reassigned
```

### Expected behavior

Each token in the linked list should correctly reference the next token in the chain. The `previous` token's `next` property should point to the newly created token, not to itself.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like it might cause issues with content traversal or serialization when the parser tries to walk through the token chain.

---
Repository: /testbed
