# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis elements (italics) in MDX when they contain nested content. The emphasis tags are rendering but the content inside them is completely empty.

### Reproduction

```mdx
This is *italic text* that should render.

This is *text with **bold** inside* that should also render.
```

When processing this MDX, the `<em>` elements are being created but they have no children - the text content just disappears.

### Expected behavior

The emphasis elements should contain their child nodes. For example:
- `*italic text*` should render as `<em>italic text</em>`
- `*text with **bold** inside*` should render as `<em>text with <strong>bold</strong> inside</em>`

Instead, I'm getting empty `<em></em>` tags with no content.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
