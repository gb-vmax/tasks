# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the parser seems to be using incorrect construct references. When parsing certain markdown content, the tokenizer appears to be initialized with the wrong parameters, causing it to not properly handle different content types.

### Reproduction

```js
// Parse markdown with mixed content types
const parser = remark();
const result = parser.parse(`
# Heading

Some paragraph text.

- List item 1
- List item 2

More content here.
`);

// The parser doesn't correctly process the different content types
// Expected proper AST with distinct nodes for headings, paragraphs, and lists
// Actual: incorrect tokenization or malformed AST
```

### Expected behavior

The parser should correctly tokenize and create an AST for different markdown constructs (headings, paragraphs, lists, etc.) by using the appropriate construct definitions for each content type.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
