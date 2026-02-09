# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where resource markers (parentheses in link syntax) are not being properly tracked in the token stream. The parser seems to be processing the closing parenthesis of a link resource, but the token events appear to be happening in the wrong order.

### Reproduction

```markdown
[link text](https://example.com)
```

When parsing this MDX content, the resource marker tokens are being generated but not in the expected sequence. The exit events for `resourceMarker` and `resource` seem to be reversed from what they should be.

### Expected behavior

The parser should properly enter and exit the `resourceMarker` token before exiting the `resource` token. The token events should maintain a proper hierarchical structure where inner tokens are closed before outer tokens.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is affecting link parsing in my MDX documents and causing issues with syntax highlighting and other tools that rely on the token structure.

---
Repository: /testbed
