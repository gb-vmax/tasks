# Bug Report

### Describe the bug

I'm encountering an issue with keyword matching in the MDX parser. It seems like certain JavaScript keywords are being incorrectly recognized or matched, causing parsing errors or unexpected behavior.

### Reproduction

When trying to parse MDX content that contains JavaScript keywords, the parser doesn't correctly identify them. For example:

```js
// MDX content with keywords like 'function', 'class', 'return', etc.
const mdxContent = `
export function MyComponent() {
  return <div>Hello</div>
}
`;

// The parser fails to properly match keywords
```

### Expected behavior

The parser should correctly match and identify JavaScript keywords like `function`, `class`, `return`, `var`, `let`, `const`, etc. when processing MDX content. The keyword matching regex should properly handle word boundaries.

### Additional context

This appears to be related to how the parser builds regular expressions for matching reserved words. The keyword matching seems to be broken, possibly affecting the entire parsing pipeline.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
