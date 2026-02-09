# Bug Report

### Describe the bug

I'm encountering an issue with keyword tokenization in the MDX parser. It appears that the token type is being set incorrectly for certain identifiers, which causes keywords to not be recognized properly during parsing.

### Reproduction

When parsing MDX content that contains JavaScript keywords (like `if`, `else`, `for`, `while`, etc.), the parser seems to treat them as regular identifiers instead of their proper keyword token types.

```js
// Example MDX content that exhibits the issue
const mdxContent = `
export const value = true;

{if (value) {
  return <div>Content</div>
}}
`;

// The parser fails to properly tokenize the 'if' keyword
// and treats it as a regular name token instead
```

### Expected behavior

Keywords should be recognized and assigned their correct token types (e.g., `if` should be tokenized as a keyword token, not a name token). The parser should properly distinguish between keywords and regular identifiers.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have broken keyword detection in JavaScript expressions within MDX files. Any help would be appreciated!

---
Repository: /testbed
