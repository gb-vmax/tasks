# Bug Report

### Describe the bug
When parsing directive containers with nested content, the linked list structure of document chunks gets corrupted. Instead of properly linking consecutive chunks, a chunk ends up pointing to itself, which breaks the document traversal and can cause infinite loops or incorrect parsing results.

### Reproduction
```js
// Parse a directive container with multiple content blocks
const markdown = `
:::note
First paragraph

Second paragraph
:::
`;

const ast = parseMarkdown(markdown);
// The document chunks are not properly linked
// Traversing the chunk chain may loop infinitely or skip content
```

### Expected behavior
Document chunks should form a proper linked list where each chunk's `next` property points to the following chunk, not to itself. The parser should correctly handle multiple content blocks within directive containers.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This seems to have broken the internal chunk linking mechanism. The parsed AST structure is malformed and subsequent processing fails.

---
Repository: /testbed
