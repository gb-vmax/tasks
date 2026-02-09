# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in MDX. When I use inline code blocks (backticks), the whitespace handling seems broken. Specifically, spaces in my inline code are being converted to newlines, which completely breaks the formatting.

### Reproduction

```mdx
This is some `inline code` with spaces.

Another example: `const foo = bar` should stay on one line.
```

When this gets rendered, the spaces inside the backticks are replaced with newlines, so instead of seeing:
```
inline code
```

I see something like:
```
inline
code
```

This is making all my inline code snippets unreadable since they're splitting across multiple lines unexpectedly.

### Expected behavior

Inline code should preserve spaces as spaces. The content between backticks should remain on a single line and not have spaces converted to newlines.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like a recent regression as it was working fine before. Any help would be appreciated!

---
Repository: /testbed
