# Bug Report

### Describe the bug

I'm experiencing an issue with blank line parsing in MDX files. It seems like line endings are being treated differently than expected, causing some blank lines to not be recognized properly.

### Reproduction

When I have MDX content with blank lines that contain only whitespace or newline characters, the parser doesn't handle them consistently. 

For example:
```mdx
Some content

Another paragraph
```

The blank line between paragraphs is sometimes not being recognized as a valid blank line, which affects the document structure and rendering.

### Expected behavior

Blank lines with line endings should be properly recognized as blank lines. The parser should accept both:
- Lines with only whitespace followed by a line ending
- Lines with just a line ending character

This is important for proper paragraph separation and maintaining the intended document structure.

### Additional context

This appears to be related to how the tokenizer handles the `after` state when checking for blank lines. The behavior seems inconsistent depending on whether the line has a line ending character or reaches EOF.

---
Repository: /testbed
