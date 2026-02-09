# Bug Report

### Describe the bug

I'm encountering an issue with blank line parsing in markdown processing. It seems like blank lines are being treated as regular content lines, and regular content lines are being treated as blank lines - essentially the opposite of what should happen.

### Reproduction

When parsing markdown with blank lines, the behavior is inverted:

```js
const markdown = `
First paragraph

Second paragraph
`;

// Blank lines between paragraphs are not recognized correctly
// Non-blank lines are being treated as blank lines instead
```

This is causing paragraph breaks to not work as expected, and content that should be parsed as separate blocks is being merged or handled incorrectly.

### Expected behavior

Blank lines (lines that are null or contain only line endings) should be recognized as blank lines and trigger appropriate parsing behavior. Non-blank lines with actual content should be treated as content lines.

Currently it seems like the logic is backwards - blank lines are being rejected and content lines are being accepted as blank lines.

### System Info
- remark version: 15.0.1
- Environment: Node.js

---
Repository: /testbed
