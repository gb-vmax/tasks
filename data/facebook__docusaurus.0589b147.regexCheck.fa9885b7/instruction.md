# Bug Report

### Describe the bug

I'm encountering an issue with character code validation in the MDX parser. It seems like certain valid whitespace characters are not being recognized properly, causing parsing to fail on content that should be valid.

### Reproduction

```js
// This should parse correctly but fails
const content = `
# Hello World

Some text with regular spaces
`;

// Parser throws an error or doesn't recognize whitespace properly
```

When I try to parse MDX content with standard whitespace characters (spaces, tabs, newlines), the parser doesn't handle them correctly. It seems like the validation logic for checking if a character code represents whitespace is broken.

### Expected behavior

The parser should correctly identify and handle all valid Unicode whitespace characters. Standard spaces, tabs, and newlines in MDX content should be processed without issues.

### Additional context

This appears to affect the `regexCheck` function used for whitespace validation. Valid character codes are being rejected when they should pass the whitespace test.

---
Repository: /testbed
