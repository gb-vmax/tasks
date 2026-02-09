# Bug Report

### Describe the bug

I'm encountering an issue with inline code parsing in markdown content. When processing markdown text that contains inline code blocks (backticks), the parser seems to be generating tokens in the wrong order, which breaks the expected AST structure.

### Reproduction

```js
const markdown = '`inline code`';
const ast = remark.parse(markdown);

// The token order is incorrect - codeTextSequence appears before codeText
// This causes issues when traversing or transforming the AST
```

When parsing inline code with backticks, the resulting token structure doesn't match what's expected. The sequence token is being created before the parent code text token, which violates the expected nesting order.

### Expected behavior

The parser should create tokens in the correct hierarchical order:
1. First enter the `codeText` token (parent)
2. Then enter the `codeTextSequence` token (child)

This is important for maintaining proper AST structure when processing markdown documents.

### Additional context

This affects any markdown content with inline code blocks. The issue appears to be in the tokenization logic for code text sequences.

---
Repository: /testbed
