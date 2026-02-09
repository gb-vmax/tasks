# Bug Report

### Describe the bug

I'm encountering an issue with keyword recognition in MDX parsing. It seems like JavaScript keywords (like `const`, `let`, `function`, etc.) are not being properly identified and are being treated as regular identifiers instead.

### Reproduction

When parsing MDX content that contains JavaScript keywords, they're being tokenized incorrectly:

```js
const content = `
export const MyComponent = () => {
  let value = 42;
  function test() {
    return value;
  }
}
`;
```

The keywords `const`, `let`, and `function` should be recognized as keyword tokens, but they're being treated as name tokens instead. This causes issues with syntax highlighting and potentially breaks certain MDX transformations.

### Expected behavior

JavaScript keywords should be properly identified and tokenized as keyword types, not as generic name tokens. The parser should recognize reserved words and handle them appropriately.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
