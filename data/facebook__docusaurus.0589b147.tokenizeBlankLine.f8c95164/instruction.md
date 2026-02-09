# Bug Report

### Describe the bug

I'm experiencing an issue with blank line parsing in MDX documents. It seems like the parser is incorrectly identifying what constitutes a blank line, causing unexpected behavior when processing markdown content.

### Reproduction

When I have MDX content with blank lines that contain only whitespace characters, the parser doesn't recognize them as blank lines. Similarly, lines that should NOT be considered blank are being treated as blank lines.

Example that triggers the issue:

```mdx
# Heading

   
Some content here

Another paragraph
```

The line with just spaces between "Heading" and "Some content here" should be recognized as a blank line, but it's not being handled correctly. Conversely, lines with actual content are sometimes being treated as blank lines when they shouldn't be.

### Expected behavior

- Lines containing only whitespace (spaces, tabs) followed by a line ending should be recognized as blank lines
- Lines with actual content should NOT be treated as blank lines
- The parser should correctly distinguish between these two cases

### System Info

- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have broken after a recent update. The logic for determining what constitutes a blank line appears to be inverted or incorrect.

---
Repository: /testbed
