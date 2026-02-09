# Bug Report

### Describe the bug

I'm experiencing incorrect position tracking when parsing MDX content with line endings. The parser seems to be calculating offsets incorrectly, which causes issues with source maps and error reporting.

### Reproduction

```js
const mdx = `# Hello

This is a test
with multiple lines
`;

// Parse the MDX content
const result = compile(mdx);

// The position offsets in the AST are incorrect
// Line ending offsets are being calculated wrong
```

### Expected behavior

The parser should correctly track character offsets when encountering line endings (both `\n` and `\r\n`). Currently, it appears to swap the offset increments for different line ending types, leading to incorrect position data in the generated AST.

This affects:
- Source map generation
- Error message line/column reporting
- Any tooling that relies on accurate position information

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
