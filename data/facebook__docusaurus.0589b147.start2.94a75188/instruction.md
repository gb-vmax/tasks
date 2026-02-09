# Bug Report

### Describe the bug

I'm experiencing an issue with link parsing in MDX content. When I use standard markdown link syntax `[text](url)`, the parser seems to be generating incorrect token structures. The links either fail to render properly or cause unexpected parsing errors in the document.

### Reproduction

```mdx
# My Document

This is a [link to example](https://example.com) in my content.

[Another link](https://test.com) here.
```

When processing this MDX content, the link tokens appear to be malformed, causing the parser to either skip the links or produce incorrect output.

### Expected behavior

Links should be parsed correctly and rendered as proper anchor tags in the output. The token structure for link markers should be properly nested and closed in the correct order.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The basic link syntax that worked before is now producing unexpected results.

---
Repository: /testbed
