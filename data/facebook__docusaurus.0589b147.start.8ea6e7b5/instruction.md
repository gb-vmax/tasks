# Bug Report

### Describe the bug

I'm encountering an issue with inline code parsing in markdown. When processing markdown text with inline code (backticks), the token structure appears to be incorrect. The `codeText` and `codeTextSequence` tokens are being generated in the wrong order, which breaks downstream processing that relies on the proper token hierarchy.

### Reproduction

```js
// Parse markdown with inline code
const markdown = 'This is `inline code` in text';
const result = parseMarkdown(markdown);

// Inspect the token structure
console.log(result.tokens);
// Expected: codeText token should wrap codeTextSequence
// Actual: codeTextSequence appears before codeText in the tree
```

### Expected behavior

The token structure should have `codeText` as the parent token with `codeTextSequence` nested inside it. This is the expected hierarchy for proper AST construction when parsing inline code blocks.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
