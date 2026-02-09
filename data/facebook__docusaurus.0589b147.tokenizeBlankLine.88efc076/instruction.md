# Bug Report

### Describe the bug

I'm experiencing an issue with blank line parsing in MDX documents. It appears that blank lines are not being recognized correctly, which is causing unexpected behavior in my MDX content rendering.

### Reproduction

When I have MDX content with blank lines (lines containing only whitespace or completely empty), they are either not being parsed as blank lines when they should be, or they're being treated as blank lines when they shouldn't be.

For example:

```mdx
# Header

Some content here

More content after blank line
```

The blank line between "Some content here" and "More content after blank line" is not being handled correctly. This affects the overall document structure and spacing in the rendered output.

### Expected behavior

Blank lines (including lines with only whitespace characters) should be properly recognized and parsed as blank lines. Lines that are not blank should not be treated as blank lines.

The parser should:
- Correctly identify lines that are null or contain line ending characters as blank lines
- Correctly handle whitespace-only lines as blank lines
- Not treat non-blank content as blank lines

### System Info
- @mdx-js/mdx version: 3.0.0

This seems to have started happening recently. The blank line tokenization logic might have been affected by a recent change.

---
Repository: /testbed
