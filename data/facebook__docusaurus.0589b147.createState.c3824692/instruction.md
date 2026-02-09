# Bug Report

### Describe the bug

I'm experiencing an issue with MDX processing where content is not being rendered correctly. It seems like child nodes in the AST are being skipped or processed in the wrong order, resulting in missing or incomplete output.

### Reproduction

When processing an MDX file with multiple child elements, some elements don't appear in the final output. For example:

```mdx
# Heading

Some paragraph text.

Another paragraph.

- List item 1
- List item 2
```

The rendered output is missing elements or they appear in unexpected order. This affects any MDX document with multiple children under a parent node.

### Expected behavior

All child elements should be processed and rendered in the correct order. The entire document structure should be preserved in the output.

### Additional context

This seems to have started recently. The issue is consistent across different MDX files and affects the rendering of nested content structures. It looks like there might be an issue with how the AST traversal is handling child nodes.

---
Repository: /testbed
