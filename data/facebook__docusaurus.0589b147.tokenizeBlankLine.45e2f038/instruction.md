# Bug Report

### Describe the bug

I'm encountering an issue with blank line parsing in MDX content. Lines that should be recognized as blank lines are not being processed correctly, and conversely, lines with content are being treated as blank lines.

### Reproduction

```mdx
# Title

This is a paragraph.

Another paragraph after a blank line.
```

When parsing the above MDX content, the blank line between paragraphs is not being handled properly. The parser seems to be treating lines with whitespace/content incorrectly versus actual blank lines.

### Expected behavior

Blank lines (lines with only whitespace or line endings) should be recognized as blank lines and trigger appropriate tokenization. Lines with actual content should not be treated as blank lines.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
