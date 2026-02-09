# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where text content in nested structures gets attached to the wrong parent node. The stack manipulation seems to be off by one level, causing text nodes to be added to an incorrect ancestor instead of their immediate parent.

### Reproduction

```mdx
<Component>
  Some text content here
  <NestedComponent>
    Nested text
  </NestedComponent>
</Component>
```

When parsing this structure, the text nodes appear to be getting pushed to the wrong level in the AST. The text "Some text content here" and "Nested text" end up in unexpected locations in the tree.

### Expected behavior

Text nodes should be added as children to their immediate parent element in the AST, not to a grandparent or other ancestor node. The stack should correctly track the current nesting level so that when `onenterdata` is called, it accesses the right parent node.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The text content is being processed but ends up in the wrong place in the resulting tree structure.

---
Repository: /testbed
