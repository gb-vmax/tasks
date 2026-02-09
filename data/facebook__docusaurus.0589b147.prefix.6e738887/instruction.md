# Bug Report

### Describe the bug

I'm experiencing an issue with whitespace handling in MDX documents. When I have multiple spaces at specific positions in my MDX content, the parser seems to be consuming one extra space character than it should, leading to incorrect parsing results.

### Reproduction

```mdx
<!-- Example MDX content with specific spacing -->
<Component>
  Content with   multiple spaces
</Component>
```

When parsing MDX content that contains sequences of spaces (particularly in certain contexts like after elements or in specific positions), the parser appears to be off by one in how it counts and processes these space characters. This results in either too many or too few spaces being consumed during parsing.

### Expected behavior

The parser should correctly handle the exact number of spaces present in the source MDX content. Space sequences should be processed accurately without consuming an extra character or stopping one character short.

### System Info
- MDX version: 3.0.0
- Environment: Node.js

This seems to be related to how the space factory function handles the limit checking when processing whitespace characters. The behavior is subtle but causes parsing inconsistencies in certain edge cases.

---
Repository: /testbed
