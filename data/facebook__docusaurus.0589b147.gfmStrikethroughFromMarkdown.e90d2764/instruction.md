# Bug Report

### Describe the bug

Strikethrough text rendering is broken in markdown parsing. When using `~~text~~` syntax, the strikethrough formatting is not being applied correctly to the output.

### Reproduction

```js
const markdown = '~~strikethrough text~~'
// Parse the markdown
const result = parseMarkdown(markdown)
// The strikethrough is not rendered properly
```

When I try to render strikethrough text using the standard GFM syntax with double tildes, the text either doesn't get the strikethrough formatting applied or renders incorrectly.

### Expected behavior

Text wrapped in `~~` should be rendered with strikethrough formatting. For example:
- Input: `~~deleted text~~`
- Expected: Text with strikethrough styling applied

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

This seems to have started recently, possibly after a recent update to the markdown parser. The strikethrough syntax worked fine in previous versions.

---
Repository: /testbed
