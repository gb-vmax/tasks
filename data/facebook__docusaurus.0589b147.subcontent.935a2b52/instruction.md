# Bug Report

### Describe the bug

I'm experiencing an issue with parsing nested content in markdown documents. When processing documents with nested structures (like lists inside blockquotes or similar), the parser seems to get stuck in an infinite loop or produces incorrect output.

### Reproduction

```js
const markdown = `
> - Item 1
>   - Nested item
> - Item 2
`;

const result = remark().parse(markdown);
// Parser hangs or produces malformed AST
```

This happens specifically with nested content structures. Simple markdown without nesting works fine, but as soon as there's any kind of nested block content, the parser behaves unexpectedly.

### Expected behavior

The parser should correctly handle nested content and produce a valid AST without hanging or producing incorrect structure.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started occurring recently. Previous versions handled this type of content without issues.

---
Repository: /testbed
