# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where text content is not being handled correctly in nested structures. When processing MDX documents with text nodes, the content appears to be getting lost or not properly appended to the correct parent node.

### Reproduction

```mdx
# Heading

Some text content here.

More text in a paragraph.
```

When parsing this MDX content, the text nodes don't seem to be getting attached to the right parent elements. The parsed output is missing text content or it's being placed in unexpected locations in the AST.

### Expected behavior

Text content should be properly parsed and attached to its parent node in the correct position within the document tree. Each text node should maintain its proper relationship with sibling and parent nodes.

### Additional context

This seems to affect basic text content parsing. The issue appears to be related to how the stack is being managed when entering data tokens during the parsing phase.

---
Repository: /testbed
