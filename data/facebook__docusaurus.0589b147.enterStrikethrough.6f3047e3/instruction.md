# Bug Report

### Describe the bug

Strikethrough text in GFM (GitHub Flavored Markdown) is being rendered as bold/strong text instead of deleted/strikethrough text. When parsing markdown with `~~text~~` syntax, the output shows bold text rather than strikethrough.

### Reproduction

```js
const markdown = '~~strikethrough text~~'
// Parse with remark-gfm

// Expected output: <del>strikethrough text</del>
// Actual output: <strong>strikethrough text</strong>
```

When processing markdown containing strikethrough syntax, the resulting AST node type is `strong` instead of `delete`, causing the text to be rendered as bold rather than with a strikethrough style.

### Expected behavior

Text wrapped in `~~` should be rendered with strikethrough styling (using `<del>` or `<s>` tags), not as bold text.

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
