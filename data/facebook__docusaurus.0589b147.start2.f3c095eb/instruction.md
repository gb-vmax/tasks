# Bug Report

### Describe the bug

I'm experiencing an issue with link parsing in MDX content. When using standard markdown link syntax `[text](url)`, the parser seems to get stuck in an infinite loop and the page becomes unresponsive.

### Reproduction

```mdx
[Click here](https://example.com)
```

When I try to render this simple markdown link, the browser freezes and I have to force quit. This is blocking me from using any links in my MDX files.

### Expected behavior

The link should be parsed correctly and rendered as a clickable anchor element without causing the parser to hang.

### System Info
- @mdx-js/mdx version: 3.0.0
- Browser: Chrome/Firefox (both affected)

This seems to have started happening recently. Basic text and other markdown features work fine, but any content with links causes the issue.

---
Repository: /testbed
