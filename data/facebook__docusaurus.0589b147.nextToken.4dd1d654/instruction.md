# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the parser doesn't properly handle the end of input. When processing MDX content, the parser seems to skip the final token in certain cases, causing incomplete parsing results.

### Reproduction

```js
const mdx = `
# Hello World

This is some content.
`;

// Parse the MDX content
const result = parseMDX(mdx);

// The last character or token is not being processed correctly
// Expected: Full AST with all content
// Actual: Missing final token/character
```

### Steps to reproduce:
1. Parse an MDX file with content that ends exactly at the input length
2. The parser terminates prematurely 
3. Final token is not included in the output

This seems to be related to how the tokenizer checks for end-of-file conditions. The behavior changed recently and now certain edge cases at the exact end of input are not being handled correctly.

### Expected behavior

The parser should process all tokens up to and including the position that equals the input length, ensuring that no content is lost during parsing.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
