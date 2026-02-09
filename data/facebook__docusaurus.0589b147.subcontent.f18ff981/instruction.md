# Bug Report

### Describe the bug

I'm experiencing issues with MDX content parsing where line breaks in nested content (like block quotes or lists) are being handled incorrectly. The parser seems to be miscalculating positions when processing multi-line tokens, causing content to be split or merged unexpectedly.

### Reproduction

```mdx
> This is a blockquote
> with multiple lines
> that should be preserved

- List item one
  with continuation
- List item two
```

When parsing this MDX content, the line breaks within the blockquote and list items aren't being tracked correctly. The output appears to have incorrect spacing or missing content between lines.

### Expected behavior

The parser should correctly handle line breaks in nested structures and maintain proper positioning of content across multiple lines. Each line within a blockquote or list item should be preserved as written.

### Additional context

This seems to affect any nested content that spans multiple lines. The issue appears to be related to how the parser calculates gaps and adjustments when processing token positions.

---
Repository: /testbed
