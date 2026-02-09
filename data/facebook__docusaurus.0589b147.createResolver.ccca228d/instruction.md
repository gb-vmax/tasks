# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where text content is not being properly resolved in certain edge cases. When processing consecutive "data" type events, some text nodes appear to be getting incorrectly merged or dropped.

### Reproduction

```js
// Parse markdown with consecutive text nodes
const processor = remark();
const ast = processor.parse('some text with **bold** and more text');

// Process the AST
const result = processor.runSync(ast);

// Expected: All text content preserved
// Actual: Some text content missing or incorrectly merged
```

### Expected behavior

All text content should be preserved when resolving consecutive data events. The text resolution logic should correctly handle boundary cases when merging adjacent text nodes.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to affect documents with inline formatting elements adjacent to plain text. The issue appears to be in the text resolution phase rather than the initial parsing.

---
Repository: /testbed
