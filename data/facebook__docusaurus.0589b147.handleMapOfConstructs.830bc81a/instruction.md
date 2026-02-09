# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain character codes are not being handled correctly. It seems like the parser is failing to process some valid markdown constructs, particularly when dealing with special characters or edge cases.

### Reproduction

```js
// Example markdown that fails to parse correctly
const markdown = `
Some text with special characters
- List item with null character handling
- Another item
`;

const result = remark().parse(markdown);
// Expected: proper AST with all list items
// Actual: some constructs are missing or incorrectly parsed
```

When parsing markdown with certain character codes, the tokenizer appears to skip or incorrectly handle some constructs. This affects list parsing and other markdown features that rely on character-level tokenization.

### Expected behavior

The parser should correctly handle all valid character codes and markdown constructs, including edge cases with special characters. All list items and other markdown elements should be properly tokenized and included in the resulting AST.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
