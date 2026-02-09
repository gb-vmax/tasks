# Bug Report

### Describe the bug

I'm experiencing an issue with MDX document processing where the flow isn't being closed properly. After a recent update, the parser seems to be leaving the container state in an inconsistent state when closing flow elements.

### Reproduction

```js
// Processing an MDX document with nested flow content
const mdxContent = `
# Heading

Some paragraph content

- List item
- Another item
`;

// Parse the document
const result = compile(mdxContent);
// The containerState._closeFlow is not being cleaned up properly
```

### Expected behavior

When closing flow elements during MDX parsing, the container state should be properly reset and all related properties should be cleared. The `_closeFlow` property on the container state should be set to `undefined` to ensure proper cleanup.

### Additional context

This seems to affect documents with multiple flow elements (headings, paragraphs, lists, etc.). The parser state isn't being fully reset between flow elements, which could lead to unexpected behavior in subsequent parsing operations.

---
Repository: /testbed
