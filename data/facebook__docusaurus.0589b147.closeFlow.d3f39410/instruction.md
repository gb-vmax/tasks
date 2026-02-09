# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the document flow isn't being closed properly. When processing markdown content with nested structures, the parser seems to maintain references that should be cleared, leading to unexpected behavior in subsequent parsing operations.

### Reproduction

```js
// Parse a document with nested block structures
const processor = remark();
const result = processor.parse(`
# Heading

> Blockquote
> with multiple lines

Another paragraph
`);

// Process another document immediately after
const result2 = processor.parse(`
Simple paragraph
`);
```

The second parse operation seems to be affected by state from the first one. The flow closing mechanism doesn't appear to be resetting properly between documents.

### Expected behavior

Each document should be parsed independently without any lingering state from previous parse operations. The flow should be completely closed and all references cleared after processing each document.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
