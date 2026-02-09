# Bug Report

### Describe the bug

I'm encountering an issue with character code validation in MDX parsing. It seems like certain valid whitespace characters are not being recognized correctly, causing the parser to fail or behave unexpectedly when processing content with specific Unicode characters.

### Reproduction

```js
// When parsing MDX content with certain whitespace characters
const content = `
# Hello

Some text with special whitespace
`;

// The parser fails to properly recognize valid whitespace codes
// This affects content with Unicode whitespace characters (e.g., non-breaking spaces, zero-width spaces)
```

The issue appears to be in the character code checking logic. When passing valid character codes that should be recognized as whitespace, they're being rejected incorrectly.

### Expected behavior

The parser should correctly identify all valid whitespace characters according to the Unicode specification. Character codes that match the whitespace regex should be properly validated and accepted.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
