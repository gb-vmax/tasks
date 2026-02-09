# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in the markdown parser. When using backticks for inline code, the output is being generated as a block code element instead of an inline code element.

### Reproduction

```js
const markdown = 'This is `inline code` in text';
const ast = parse(markdown);

// The code node has incorrect type
console.log(ast.children[0].children[1]);
// Expected: { type: 'inlineCode', value: 'inline code' }
// Actual: { type: 'code', value: 'inline code', inline: false }
```

### Expected behavior

Inline code (text wrapped in single backticks) should be represented as `inlineCode` nodes in the AST, not as `code` nodes with `inline: false`. The `code` type should be reserved for fenced code blocks.

This is causing issues with rendering because inline code is being treated as a block-level element, which breaks the flow of text and adds unwanted line breaks.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
