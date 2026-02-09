# Bug Report

### Describe the bug

I'm experiencing an issue with MDX link parsing where links in my markdown documents are not being rendered correctly. The links appear to be broken or not showing up at all in the output.

### Reproduction

```mdx
# My Document

Here's a [link to example](https://example.com) that should work.

[Another link](https://test.com) with some text.
```

When I compile this MDX content, the links don't render properly. Instead of getting clickable links, I'm either getting nothing or broken output.

### Expected behavior

Links should be parsed correctly and rendered as proper anchor tags with the correct href attributes and link text as children.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
