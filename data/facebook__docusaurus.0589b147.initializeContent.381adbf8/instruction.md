# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where the order of operations seems to be affecting the token linking and text chunk processing. When parsing markdown content with line endings, the tokens aren't being properly connected in the expected sequence.

### Reproduction

```js
// Parse markdown content with text chunks and line breaks
const markdown = `Some text content
with line breaks
and multiple lines`;

const result = parseMarkdown(markdown);

// The token chain appears to be broken or incorrectly ordered
// Expected: tokens should be linked with proper previous/next references
// Actual: token relationships are inconsistent
```

### Expected behavior

When parsing markdown text with line endings:
1. Tokens should be linked correctly with their previous/next references set in the right order
2. Text chunks should be properly exited before consuming line ending characters
3. The token chain should maintain proper sequential relationships

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to affect how the content tokenization flow works, particularly around text chunks and line endings. The previous token assignment and the exit/consume order for chunks might be happening in an unexpected sequence.

---
Repository: /testbed
