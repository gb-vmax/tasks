# Bug Report

### Describe the bug

I'm experiencing an issue with blank line detection in MDX parsing. It seems like the parser is incorrectly identifying what constitutes a blank line, causing unexpected behavior when processing MDX content.

### Reproduction

```js
// MDX content with blank lines
const mdxContent = `
# Title

Some content here

More content after blank line
`

// Parse the MDX content
// Expected: Blank lines should be properly recognized
// Actual: Lines that should be blank are not being treated as blank lines
```

When parsing MDX documents with blank lines between content blocks, the parser appears to be treating actual blank lines as non-blank lines and vice versa. This causes issues with proper content separation and formatting.

### Expected behavior

Blank lines (lines containing only whitespace or line endings) should be correctly identified as blank lines, and non-blank lines should be identified as non-blank lines. The parser should properly handle spacing between content blocks in MDX documents.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This is affecting our MDX documentation rendering and causing formatting issues throughout our docs.

---
Repository: /testbed
