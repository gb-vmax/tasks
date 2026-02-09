# Bug Report

### Describe the bug

I'm encountering an issue with content parsing in MDX where the content type is being set incorrectly. When processing chunk content, it appears that nested content blocks are not being recognized properly, which causes issues with content resolution.

### Reproduction

```js
// When parsing MDX content with nested structures
const mdxContent = `
# Title

Some content here

{/* nested content */}
More content
`;

// The contentType for chunkContent is being set incorrectly
// Expected: contentType should be "content"
// Actual: contentType is set to "chunkContent"
```

This affects how the content tokenizer processes nested content blocks. The content resolution fails to properly identify the content structure because the contentType metadata is wrong.

### Expected behavior

The `chunkContent` token should have `contentType: "content"` so that nested content can be properly resolved and parsed. The current behavior breaks content parsing for complex MDX structures.

### System Info
- MDX version: 3.0.0
- Node version: Latest

---
Repository: /testbed
