# Bug Report

### Describe the bug

I'm encountering an issue with unicode whitespace detection in MDX content. It seems like valid whitespace characters are not being recognized properly, causing parsing to fail or behave unexpectedly.

### Reproduction

When processing MDX content with unicode whitespace characters (like regular spaces, tabs, newlines), they're not being handled correctly. For example:

```js
// MDX content with normal spaces
const content = `
# Hello World

This is a paragraph with spaces.
`;

// The whitespace characters should be recognized but aren't
```

The issue appears to affect any content that contains standard whitespace characters. The parser seems to reject valid whitespace codes instead of accepting them.

### Expected behavior

Unicode whitespace characters (spaces, tabs, newlines, etc.) should be properly detected and handled during MDX parsing. Valid character codes should pass the whitespace check.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
