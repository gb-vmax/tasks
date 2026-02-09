# Bug Report

### Describe the bug

I'm experiencing an issue with blank line parsing in MDX content. It seems like the parser is incorrectly handling blank lines in certain scenarios, causing unexpected behavior when rendering MDX documents.

### Reproduction

When I have MDX content with blank lines, they're not being recognized properly:

```mdx
Some content here

Another paragraph after a blank line
```

The blank line between paragraphs is either being treated as non-blank content or being rejected when it should be accepted. This causes the MDX parser to fail or produce incorrect output.

### Expected behavior

Blank lines (lines containing only whitespace or line endings) should be properly recognized and handled by the parser. The content should parse correctly with proper paragraph separation.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
