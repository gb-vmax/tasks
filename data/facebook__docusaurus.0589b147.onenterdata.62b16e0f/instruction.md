# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where text nodes are not being created properly in certain cases. It seems like the parser is pushing the wrong node onto the stack, which causes text content to either be lost or incorrectly structured in the AST.

### Reproduction

```mdx
# Heading

Some text content here.

More text in another paragraph.
```

When parsing MDX content with multiple text nodes, the text content doesn't appear in the output or gets attached to the wrong parent node. The issue seems to occur specifically when handling consecutive text data tokens.

### Expected behavior

Text nodes should be properly created and added to the AST. Each text segment should maintain its correct parent-child relationship in the tree structure.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
