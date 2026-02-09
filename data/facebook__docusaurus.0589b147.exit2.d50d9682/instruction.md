# Bug Report

### Describe the bug

I'm experiencing incorrect behavior with nested token parsing in markdown content. When processing nested structures (like lists within lists or nested emphasis), the tokens are being closed in the wrong order, leading to malformed parse trees.

### Reproduction

```js
const markdown = `
- Outer list item
  - Nested list item
    - Deeply nested item
`;

const result = remark.parse(markdown);
// The token structure is incorrect - tokens are closed in FIFO order instead of LIFO
```

Another example with nested emphasis:

```js
const markdown = `**bold *italic* text**`;
const result = remark.parse(markdown);
// Inner tokens are closed before outer tokens, breaking the nesting structure
```

### Expected behavior

Tokens should be closed in Last-In-First-Out (LIFO) order to properly maintain the nesting hierarchy. The innermost tokens should be closed first, working outward to the outermost tokens.

Currently, it appears tokens are being closed in First-In-First-Out (FIFO) order, which breaks the proper nesting structure of the AST.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
