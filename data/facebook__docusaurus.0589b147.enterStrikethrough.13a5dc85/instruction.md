# Bug Report

### Describe the bug

Strikethrough text in GFM (GitHub Flavored Markdown) is being rendered as emphasized/italic text instead of strikethrough. When parsing markdown with `~~text~~` syntax, the output shows emphasis formatting rather than the expected delete/strikethrough formatting.

### Reproduction

```js
// Parse markdown with strikethrough
const markdown = "This is ~~deleted~~ text";
const result = parseMarkdown(markdown);

// Expected: { type: "delete", children: [...] }
// Actual: { type: "emphasis", children: [...] }
```

When rendering this, the text appears italicized instead of having a strikethrough line through it.

### Expected behavior

Text wrapped in `~~` should be converted to a node with `type: "delete"` which renders as strikethrough, not `type: "emphasis"` which renders as italic/emphasized text.

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
