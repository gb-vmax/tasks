# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where text nodes are not being handled correctly. When parsing markdown content with inline text, the parser seems to crash or produce malformed output.

### Reproduction

```js
const markdown = `
# Heading

This is some text content.
`;

const result = remark().parse(markdown);
// Parser throws error or produces incorrect AST
```

### Expected behavior

The parser should correctly process text content and create proper text nodes in the AST. Text content should be appended to the appropriate parent node without errors.

### Additional context

This seems to affect any markdown document that contains regular text content (not just special elements like headings or lists). The issue appears when the parser tries to handle inline text data.

---
Repository: /testbed
