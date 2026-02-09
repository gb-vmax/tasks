# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where nested text content is not being handled correctly. It appears that text nodes are being attached to the wrong parent element in the AST, causing the document structure to break.

### Reproduction

```mdx
# Heading

Some paragraph text with **bold** content.

Another paragraph.
```

When parsing this MDX content, the text nodes end up in unexpected positions in the syntax tree. The structure becomes malformed and subsequent content may not render properly or appear in the wrong location.

### Expected behavior

Text content should be properly nested under their correct parent nodes. Each paragraph should contain its text as direct children, and the overall document structure should be preserved correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
