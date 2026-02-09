# Bug Report

### Describe the bug

I'm experiencing an issue with blank line parsing in MDX documents. It seems like blank lines are not being recognized correctly, which is causing unexpected behavior in my markdown parsing.

### Reproduction

```mdx
# Header

Content here

Another paragraph
```

When I have multiple blank lines or blank lines at the end of the document, they're not being handled as expected. The parser seems to be treating them differently than it should.

### Expected behavior

Blank lines should be properly recognized and processed. Whether the line ending is `null` or an actual line ending character, the parser should handle both cases correctly and allow blank lines to be parsed as valid blank lines.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to have started recently, possibly after a recent update to the tokenizer logic. The blank line detection seems to be inverted or using the wrong logical operator.

---
Repository: /testbed
