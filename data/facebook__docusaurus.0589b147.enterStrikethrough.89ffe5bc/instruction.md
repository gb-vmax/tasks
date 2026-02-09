# Bug Report

### Describe the bug

Strikethrough text is being rendered as emphasis/italics instead of being rendered with a strikethrough style. When parsing GFM (GitHub Flavored Markdown) strikethrough syntax (text wrapped in `~~`), the output shows emphasized text rather than deleted/strikethrough text.

### Reproduction

```js
// Input markdown with strikethrough
const markdown = "This is ~~strikethrough~~ text"

// After parsing, the strikethrough portion is converted to emphasis
// instead of delete/strikethrough
```

When processing markdown with strikethrough syntax like `~~example~~`, the text appears italicized instead of having a line through it.

### Expected behavior

Text wrapped in `~~` should be rendered with strikethrough styling (as a `delete` element), not as emphasized/italic text.

**Example:**
- Input: `~~strikethrough~~`
- Expected: ~~strikethrough~~ (with strikethrough)
- Actual: *strikethrough* (italicized)

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
