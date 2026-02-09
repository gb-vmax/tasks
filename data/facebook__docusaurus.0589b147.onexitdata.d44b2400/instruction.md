# Bug Report

### Describe the bug

I'm experiencing issues with MDX content parsing where text data is being placed in the wrong location in the AST. It seems like when processing data tokens, the content ends up attached to an incorrect parent node rather than the expected one.

### Reproduction

When parsing MDX content with nested elements and text nodes, the text content appears to be misaligned or attached to the wrong element in the resulting structure. For example:

```mdx
<Component>
  Some text content here
  <NestedComponent />
</Component>
```

The text "Some text content here" gets associated with the wrong node in the tree, causing rendering issues or unexpected output.

### Expected behavior

Text content should be correctly associated with its immediate parent element in the AST. The data should be appended to the correct node and position information should accurately reflect the token's actual location.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently and is affecting content that was previously rendering correctly. The position tracking also seems off - end positions are pointing to start locations instead.

---
Repository: /testbed
