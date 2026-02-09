# Bug Report

### Describe the bug

I'm experiencing an issue with code text parsing where inline code blocks are not being properly resolved. It seems like the parser is cutting off the last character or not including all the content within backticks.

### Reproduction

When parsing MDX content with inline code, the code text resolution appears to be off by one character. For example:

```js
const mdxContent = `
This is some text with \`inline code\` in it.
`;

// The inline code content is not being captured correctly
// Expected: "inline code"
// Actual: "inline cod" or similar truncation
```

### Expected behavior

Inline code blocks enclosed in backticks should be fully captured and rendered with all characters intact. The parser should correctly identify the start and end boundaries of code text tokens.

### Additional context

This seems to affect any inline code usage in MDX documents. The issue appears to be related to how the code text events are being indexed and resolved during parsing.

---
Repository: /testbed
