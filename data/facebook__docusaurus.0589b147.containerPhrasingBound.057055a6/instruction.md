# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where phrasing content isn't being handled correctly. When parsing certain markdown structures, the content appears to be processed in the wrong order or context.

### Reproduction

```js
const processor = remark();
const result = processor.processSync('Some **bold** text');
```

When processing markdown with inline formatting (like bold, italic, etc.), the parser seems to be passing arguments in an unexpected order internally, which leads to incorrect AST generation or processing failures.

### Expected behavior

The markdown processor should correctly handle phrasing content (inline elements) within container elements. The parent-child relationship should be maintained properly during parsing.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
