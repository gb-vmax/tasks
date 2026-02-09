# Bug Report

### Describe the bug

Strikethrough syntax in markdown is not being parsed correctly. When using the `~~` delimiter for strikethrough text, the markdown parser fails to recognize it properly and the text doesn't get rendered with strikethrough formatting.

### Reproduction

```js
const markdown = '~~strikethrough text~~'
// Expected: text should be wrapped in strikethrough tags
// Actual: text is rendered as plain text with ~~ visible
```

When processing markdown with double tildes, the parser doesn't apply the strikethrough formatting. The `~~` characters remain visible in the output instead of being converted to the appropriate strikethrough HTML/formatting.

### Expected behavior

Text wrapped in `~~` should be rendered with strikethrough formatting. The tildes should be consumed by the parser and the content should be marked as strikethrough.

Example:
- Input: `~~deleted text~~`
- Expected output: <del>deleted text</del>
- Actual output: ~~deleted text~~

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
