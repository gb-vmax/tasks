# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where content with line breaks is not being processed correctly. The parser seems to be miscalculating offsets when handling multi-line content blocks, leading to incorrect token positioning.

### Reproduction

When parsing MDX content that contains elements spanning multiple lines, the parser produces incorrect results. For example:

```mdx
<Component
  prop="value"
>
  Content here
</Component>
```

The parser appears to be calculating jump offsets incorrectly, which causes downstream issues with how the content is tokenized and processed.

### Expected behavior

The parser should correctly handle multi-line content and maintain accurate token positions throughout the parsing process. Elements that span multiple lines should be processed with the correct offset calculations.

### Additional context

This seems related to how the subcontent function handles event indexing and gap calculations. The issue manifests when there are breaks in the token stream across multiple lines.

---
Repository: /testbed
