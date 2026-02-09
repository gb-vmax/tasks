# Bug Report

### Describe the bug

I'm experiencing an issue with MDX rendering where an extra blank line is being added at the end of container flow elements. This appears to be affecting the output formatting of my MDX documents.

### Reproduction

When rendering MDX content with container flow elements (like lists, blockquotes, or other block-level content), there's an unexpected newline being appended after the last child element.

```mdx
<div>
  - Item 1
  - Item 2
  - Item 3
</div>
```

The output now includes an extra blank line after the last item that wasn't there before.

### Expected behavior

The container should not add trailing newlines after the last child element. The formatting should match the input structure without additional blank lines at the end of the container.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
