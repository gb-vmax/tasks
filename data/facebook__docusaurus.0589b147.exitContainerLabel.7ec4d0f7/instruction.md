# Bug Report

### Describe the bug

I'm encountering an issue with the remark-directive parser where container labels are being exited twice, causing the parser state to become corrupted. This leads to unexpected behavior when processing markdown directives with labels.

### Reproduction

```js
const directive = `
:::note{label="Important"}
Some content here
:::
`;

// Parse the directive
const result = parseMarkdown(directive);
// Parser exits the label token twice, corrupting the AST
```

### Expected behavior

The parser should exit each token exactly once. Container labels should be properly closed without double-exiting the token, maintaining correct parser state throughout the parsing process.

### Additional context

This appears to affect any container directive that includes a label attribute. The issue manifests as malformed AST output where the tree structure doesn't match the expected hierarchy.

---
Repository: /testbed
