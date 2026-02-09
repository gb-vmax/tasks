# Bug Report

### Describe the bug

I'm experiencing an issue with blank line parsing in MDX content. It seems like the parser is incorrectly handling whitespace-only lines and line endings, causing unexpected behavior when processing markdown documents.

### Reproduction

```mdx
Some content here

   
Another paragraph
```

When parsing the above MDX content with blank lines (including lines with only spaces), the parser behaves unexpectedly. Lines that should be recognized as blank lines are not being processed correctly, and vice versa.

### Expected behavior

The parser should correctly identify and handle:
1. Lines with only whitespace characters as blank lines
2. Lines with actual line ending characters (like `\n`) as blank lines
3. Properly distinguish between these cases and non-blank content

Currently, it seems like the logic for determining what constitutes a blank line is inverted or incorrectly applied during tokenization.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
