# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where certain character codes are not being handled correctly. It seems like null/undefined character codes are being processed incorrectly, which causes the parser to fail or behave unexpectedly in specific edge cases.

### Reproduction

When parsing MDX content that contains specific character sequences, the tokenizer doesn't properly handle the character codes. This appears to happen when the parser encounters certain boundary conditions.

```js
// Example MDX content that triggers the issue
const mdxContent = `
# Title

Some content with special characters or edge cases
`;

// The parser fails to correctly tokenize when encountering null character codes
```

### Expected behavior

The tokenizer should correctly handle all character codes, including null values, and properly construct the token list. The parser should be able to process MDX content without failing on edge cases.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
