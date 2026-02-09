# Bug Report

### Describe the bug

I'm encountering an issue with text parsing where the parser seems to be entering the wrong token type. When processing content that should be treated as "data", it appears to be incorrectly labeled as "text" instead, which is causing downstream parsing problems.

### Reproduction

```js
// Parse markdown content with text nodes
const processor = remark();
const result = processor.parse('some text content');

// The AST shows incorrect token types for data nodes
// Expected: nodes with type "data"
// Actual: nodes are being marked as "text" instead
```

This seems to happen specifically when the parser encounters content that isn't at a break point. The token type being assigned doesn't match what the rest of the parsing logic expects.

### Expected behavior

Text content should be properly categorized with the correct token type ("data") so that subsequent parsing stages can handle it appropriately. The token type mismatch is causing issues with how the content is being processed.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
