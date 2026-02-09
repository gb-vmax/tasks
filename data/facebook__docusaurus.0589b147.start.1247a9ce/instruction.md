# Bug Report

### Describe the bug

I'm experiencing an issue with blank line detection in markdown parsing. It seems like blank lines are being incorrectly identified - lines that should be recognized as blank lines are not being detected, and vice versa.

### Reproduction

When parsing markdown content with blank lines, the parser behaves unexpectedly:

```js
// Example markdown with blank lines
const markdown = `
First paragraph

Second paragraph
`;

// The blank line between paragraphs is not being recognized correctly
// This affects paragraph separation and document structure
```

The issue appears to be related to how whitespace is being checked at the start of lines. Lines with spaces are being treated as blank when they shouldn't be, or blank lines are not being recognized when they should be.

### Expected behavior

Blank lines should be correctly identified:
- A line containing only whitespace characters should be treated as a blank line
- Lines with actual content (even if preceded by spaces) should not be treated as blank lines
- This should properly separate paragraphs and other block-level elements in the parsed output

### System Info
- remark version: 15.0.1
- Running in Jest environment

---
Repository: /testbed
