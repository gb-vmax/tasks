# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the content structure appears to be incorrect. When parsing certain markdown content, the token tree seems to have nodes in the wrong order, which is causing downstream processing issues.

### Reproduction

```js
// Parse markdown with content blocks
const result = remark().parse(`
Some content here
with multiple lines
`);

// The AST structure has 'content' and 'chunkContent' tokens
// but they appear to be in an unexpected order
```

When inspecting the token tree, the `content` token appears before `chunkContent`, but based on the expected structure, `chunkContent` should be entered first since it contains the actual content data.

### Expected behavior

The token tree should have `chunkContent` entered before `content` to maintain proper nesting and content type hierarchy. The current ordering breaks assumptions about the token structure in subsequent processing steps.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
