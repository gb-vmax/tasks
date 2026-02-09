# Bug Report

### Describe the bug

I'm experiencing an issue with token position tracking in the MDX parser. It appears that token end positions are being set incorrectly, which causes the parser to report wrong source locations for syntax elements.

### Reproduction

When parsing MDX content, the token positions don't match the actual character positions in the source text. This becomes apparent when trying to:

1. Get accurate error messages with correct line/column numbers
2. Use source maps for debugging
3. Build tooling that relies on precise token locations

Example scenario:
```js
// Parse some MDX content
const result = compile('# Hello\n\nSome text here')

// Check token positions - they don't align with actual source positions
// Token end position points to the start instead of the end
```

### Expected behavior

Token end positions should point to the actual end of the token in the source text, not to the start position. This is critical for:
- Accurate error reporting
- Proper source map generation  
- Tools that need to extract or highlight specific parts of the source

The `prevType` context also seems to be tracked incorrectly, which could affect how the parser handles context-sensitive syntax.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
