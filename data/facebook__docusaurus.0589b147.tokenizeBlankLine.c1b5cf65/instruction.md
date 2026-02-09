# Bug Report

### Describe the bug

I'm experiencing an issue with blank line parsing in MDX documents. It seems like blank lines are not being recognized correctly, which is causing problems with document structure and rendering.

### Reproduction

```mdx
# Heading

Some paragraph text here.

Another paragraph after a blank line.
```

When processing this MDX content, the blank line between the paragraphs is not being handled properly. The parser seems to be treating non-space characters as if they should trigger blank line processing, and it's also checking for line endings when it shouldn't.

### Expected behavior

Blank lines (lines containing only whitespace or completely empty) should be properly tokenized and recognized. The parser should:
1. Correctly identify when a line contains only spaces/whitespace
2. Properly handle line endings in the context of blank lines
3. Maintain proper document structure with paragraph separation

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is affecting document parsing and the resulting output structure. Any help would be appreciated!

---
Repository: /testbed
