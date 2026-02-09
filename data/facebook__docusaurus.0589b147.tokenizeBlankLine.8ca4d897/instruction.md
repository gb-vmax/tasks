# Bug Report

### Describe the bug

I'm encountering an issue with blank line parsing in markdown content. When processing markdown documents with blank lines that contain only whitespace characters, the parser is not handling them correctly. Lines that should be recognized as blank lines are being rejected, causing parsing failures.

### Reproduction

```js
const markdown = `
First paragraph

  
Second paragraph
`;

// Parse the markdown
const result = remark.parse(markdown);
// The blank line with spaces is not being recognized properly
```

The issue occurs specifically when:
1. A blank line contains whitespace characters (spaces/tabs)
2. The parser tries to tokenize these lines
3. The line should be treated as a valid blank line but isn't

### Expected behavior

Blank lines containing only whitespace characters should be properly recognized and processed as blank lines. The parser should accept lines that are either:
- Completely empty (just a line ending)
- Contain only whitespace characters followed by a line ending

Both cases should be treated equivalently as blank lines in the markdown structure.

### System Info
- remark version: 15.0.1
- Environment: Node.js

---
Repository: /testbed
