# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where line endings are not being detected correctly. It seems like the parser is failing to recognize newlines and treating them as regular characters instead.

### Reproduction

```js
const markdown = `
This is line one
This is line two

This is after a blank line
`;

// Parser fails to recognize line breaks
// Everything gets treated as a single line
```

When parsing markdown with line breaks, the content is not being split properly. The parser appears to be checking for line endings incorrectly, causing multi-line markdown to be treated as a single continuous line.

### Expected behavior

The parser should correctly identify line ending characters (newlines, carriage returns) and handle them appropriately. Each line should be parsed separately and blank lines should create proper paragraph breaks.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This is causing issues with any markdown that contains multiple lines or paragraphs. The logic for detecting line endings seems to be inverted or incorrect.

---
Repository: /testbed
