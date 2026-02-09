# Bug Report

### Describe the bug

I'm experiencing an issue with content tokenization where the token types appear to be emitted in the wrong order. When processing markdown content, the `content` and `chunkContent` tokens are being created in an unexpected sequence, which is causing problems with parsing nested content structures.

### Reproduction

```js
// When tokenizing content chunks, the following occurs:
// 1. chunkContent token is entered first
// 2. content token is entered second (and assigned to previous2)
// 
// This appears to be backwards from what's expected

const processor = remark();
const result = processor.parse(`
Some content with nested structures
`);

// The token tree structure shows content/chunkContent in reversed order
// Expected: content -> chunkContent
// Actual: chunkContent -> content
```

### Expected behavior

The `content` token should be entered before `chunkContent` since `chunkContent` should be nested inside the `content` token. The current order breaks the expected token hierarchy.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
