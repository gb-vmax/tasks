# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the content type for text chunks is being set incorrectly. When processing paragraph content, the chunks are getting labeled with the wrong content type which causes downstream parsing issues.

### Reproduction

```js
// Parse a simple paragraph
const processor = remark();
const result = processor.parse('This is a test paragraph');

// Inspect the token structure
// The chunkText tokens have contentType: "chunkText" instead of "text"
```

When parsing markdown paragraphs, the text chunk tokens are created with an incorrect `contentType` property. This seems to affect how the content is processed in later stages of the pipeline.

### Expected behavior

Text chunks within paragraphs should have `contentType: "text"` so they're properly recognized as text content by the parser. The current behavior breaks the expected token structure.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
