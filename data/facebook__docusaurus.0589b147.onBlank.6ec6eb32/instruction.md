# Bug Report

### Describe the bug

I just updated to the latest version and now my MDX files are completely broken. The parser seems to be failing when processing list items with blank lines. I'm getting syntax errors that don't make any sense.

### Reproduction

```mdx
- First item
  
  Continuation paragraph

- Second item
```

When I try to parse this MDX content, it throws an error. The same content worked perfectly fine in the previous version.

### Expected behavior

The parser should handle list items with blank lines and continuation paragraphs correctly, just like it did before the update.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is blocking my entire project right now. Any help would be appreciated!

---
Repository: /testbed
