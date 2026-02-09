# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where content inside lists and other nested structures is not being properly converted to strings. The output appears to be returning unexpected values instead of the actual text content.

### Reproduction

```js
// When parsing MDX with nested list items
const mdxContent = `
- First item
- Second item
  - Nested item
`;

// The parsed output doesn't contain the expected string content
// Instead getting malformed or incomplete text
```

### Expected behavior

The parser should correctly extract and return the string content from nested structures. Each list item and nested element should be properly converted to its string representation.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have broken recently. The text content is being processed incorrectly when the parser tries to resume from the stack.

---
Repository: /testbed
