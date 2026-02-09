# Bug Report

### Describe the bug

After a recent update, markdown parsing is broken when processing whitespace in certain contexts. Documents that previously parsed correctly are now failing to render properly, particularly when dealing with spaces at the beginning of lines or in specific formatting contexts.

### Reproduction

```js
// Example markdown that fails to parse correctly
const markdown = `
  Some indented text
  
  * List item with spaces
  * Another item
`;

// The parser gets stuck or produces unexpected output
const result = parseMarkdown(markdown);
```

### Expected behavior

The markdown parser should correctly handle whitespace and produce the expected AST/output. Indented text and list items with leading spaces should be processed without issues.

### Additional context

This seems to affect the `factorySpace` function in the GFM plugin. The parser appears to get into an incorrect state when encountering markdown spaces, causing it to either hang or produce malformed output.

---
Repository: /testbed
