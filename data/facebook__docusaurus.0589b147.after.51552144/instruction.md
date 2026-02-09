# Bug Report

### Describe the bug

I'm experiencing an issue with blank line parsing in markdown content. It seems like blank lines are not being recognized correctly, which is causing unexpected behavior when processing markdown documents.

### Reproduction

```js
const markdown = `
First paragraph

Second paragraph
`;

// Process the markdown
const result = remark().parse(markdown);

// The blank line between paragraphs is not being handled correctly
// Expected: Two separate paragraph nodes
// Actual: Content is being merged or parsed incorrectly
```

### Expected behavior

Blank lines (lines containing only whitespace or nothing) should be properly detected and used to separate content blocks like paragraphs. The parser should recognize both:
- Lines that are completely empty (null/EOF)
- Lines that end with a line ending character

Currently it seems like one of these cases is not being handled properly.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
