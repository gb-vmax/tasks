# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in MDX. When using backticks for inline code, the parser seems to be entering an infinite loop or hanging indefinitely. The browser tab becomes unresponsive and I have to force close it.

### Reproduction

```mdx
This is some text with `inline code` in the middle.
```

When I try to render this MDX content, the page freezes and never finishes loading. It seems to happen specifically with inline code blocks using single or multiple backticks.

### Expected behavior

The inline code should be parsed correctly and rendered as expected, like:
- This is some text with `inline code` in the middle.

The parser should handle the opening backtick sequence, capture the code content, find the closing backtick sequence, and move on to parse the rest of the document.

### System Info
- @mdx-js/mdx version: 3.0.0
- Browser: Chrome/Firefox (happens on both)

This is blocking our documentation site from working. Any help would be appreciated!

---
Repository: /testbed
