# Bug Report

### Describe the bug

I'm encountering an issue with keyword recognition in the MDX parser. It appears that regular JavaScript keywords are not being properly identified and are instead being treated as regular identifiers/names.

### Reproduction

```js
// When parsing MDX content with JavaScript keywords
const mdxContent = `
export const myVar = true;
if (condition) {
  return value;
}
`;

// Keywords like 'export', 'const', 'if', 'return' are being 
// tokenized as names instead of their proper keyword types
```

### Expected behavior

JavaScript keywords should be recognized and tokenized with their appropriate keyword token types, not as generic name tokens. For example:
- `export` should be tokenized as a keyword token
- `const` should be tokenized as a keyword token  
- `if` should be tokenized as a keyword token
- `return` should be tokenized as a keyword token

Currently they're all being treated as regular identifiers which breaks parsing of valid JavaScript/MDX code.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
