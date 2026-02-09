# Bug Report

### Describe the bug
I'm experiencing an issue with inline code parsing in MDX content. When using backticks for inline code (`` `code` ``), the parser seems to be entering tokens in the wrong order, which causes the resulting AST structure to be incorrect.

### Reproduction
```js
const mdx = `
This is some text with \`inline code\` in it.
`;

// Parse the MDX content
const result = compile(mdx);

// The AST shows tokens entered in wrong order:
// - codeTextSequence is entered before codeText
// - This breaks the expected token hierarchy
```

### Expected behavior
The parser should enter the `codeText` token first, then the `codeTextSequence` token, to maintain the correct parent-child relationship in the AST. The current behavior has them reversed which breaks downstream processing that relies on the proper token structure.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to have broken after a recent change to the tokenizer. The token entry order is critical for proper AST construction.

---
Repository: /testbed
