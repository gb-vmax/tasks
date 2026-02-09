# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in MDX. When I have inline code that contains newlines or carriage returns, they're being converted to spaces as expected. However, after a recent update, something seems broken - the inline code is now showing unexpected behavior where spaces are being replaced with newlines instead.

### Reproduction

```mdx
This is some `inline code with spaces` in the text.
```

When this gets rendered, the spaces inside the inline code block are being replaced with newlines, which breaks the formatting completely. The code that should appear on a single line is now split across multiple lines.

### Expected behavior

Inline code should preserve spaces and convert any newlines/carriage returns to spaces (so everything stays on one line). Instead, it's doing the opposite - replacing spaces with newlines.

For example:
- Input: `` `hello world test` ``
- Expected output: `hello world test` (on one line)
- Actual output: The text appears broken with newlines between words

This is causing inline code snippets to render incorrectly throughout my documentation.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
