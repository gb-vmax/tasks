# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the parser seems to be consuming tokens even when they don't match the expected type. This is causing the parser to skip over tokens incorrectly and produce malformed output.

### Reproduction

```js
// Example MDX content that triggers the issue
const mdxContent = `
# Heading

Some text with **bold** formatting.

- List item 1
- List item 2
`;

// When parsing this content, tokens are being consumed 
// even when they shouldn't be, leading to incorrect AST structure
```

The parser appears to be advancing through tokens regardless of whether they match the expected type, which breaks the parsing logic for various MDX constructs.

### Expected behavior

The parser should only consume/advance to the next token when the current token matches the expected type. If the token doesn't match, it should return false without advancing the parser state.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
