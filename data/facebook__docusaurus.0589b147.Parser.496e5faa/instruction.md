# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where line and column tracking appears to be off by one. When parsing MDX content with a custom `startPos`, the parser seems to be calculating the `lineStart` position incorrectly, which leads to wrong line/column numbers in error messages and source maps.

### Reproduction

```js
const { compile } = require('@mdx-js/mdx');

const mdxContent = `
# Hello World

This is some MDX content
`;

// Parse starting from a specific position
const result = compile(mdxContent, {
  // Parser initialized with startPos
});

// Line numbers in errors or source maps are off by one
```

When the parser is initialized with a `startPos` parameter, the line start calculation doesn't account for the position correctly. This causes subsequent line/column calculations to be inaccurate.

### Expected behavior

The parser should correctly track line and column positions regardless of the `startPos` value. Error messages and source maps should report accurate line numbers that match the actual content.

### System Info

- @mdx-js/mdx version: 3.0.0
- Node.js version: Latest

This seems to affect any scenario where the parser needs to track positions within the source, particularly when using features that rely on accurate source mapping.

---
Repository: /testbed
