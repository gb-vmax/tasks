# Bug Report

### Describe the bug

I'm experiencing an issue with MDX rendering where newline characters in table elements are being processed incorrectly. When rendering tables, the output seems to include unexpected text nodes or skip content that should be rendered.

### Reproduction

```js
const mdx = `
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
`

// When compiling this MDX table, the output is malformed
// Newlines that should be ignored are being processed
// and regular content is being skipped
```

### Expected behavior

Tables should render cleanly with proper handling of whitespace and newline characters. Text content within table cells should be preserved while structural newlines between table elements should be ignored appropriately.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have broken recently - tables were rendering fine before. The issue appears to be related to how text nodes are being filtered in table contexts.

---
Repository: /testbed
