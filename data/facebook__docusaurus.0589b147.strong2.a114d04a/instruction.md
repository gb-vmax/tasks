# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX compiler where strong/bold elements (`**text**`) are causing unexpected behavior. When rendering MDX content with bold text, the output is malformed and causes infinite loops or crashes.

### Reproduction

```mdx
This is **bold text** in my document.
```

When processing this MDX content, the compiler seems to generate invalid AST nodes for the strong elements. The resulting output is corrupted and doesn't render properly.

### Expected behavior

Bold text should be parsed and rendered correctly as `<strong>` elements in the final output. The AST node for strong elements should have a proper structure with a `type` property set to `"strong"` and a `children` array containing the nested text nodes.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems like a regression as bold text was working fine in previous versions. Any help would be appreciated!

---
Repository: /testbed
