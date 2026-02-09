# Bug Report

### Describe the bug

I'm encountering an issue with blank line parsing in markdown content. It seems like the parser is incorrectly handling blank lines - lines that should be recognized as blank are being treated as non-blank, and vice versa.

### Reproduction

```js
// Example markdown with blank lines
const markdown = `
First paragraph

Second paragraph
`;

// Parse the markdown
const result = remark.parse(markdown);

// The blank line between paragraphs is not being recognized correctly
// This causes the two paragraphs to be merged or handled improperly
```

Another case:
```js
// Lines with only whitespace should be treated as blank
const markdown = `Line 1
   
Line 2`;

// The line with spaces is not being recognized as a blank line
```

### Expected behavior

- Lines containing only whitespace (spaces, tabs) should be recognized as blank lines
- Actual blank lines (with line endings) should be properly tokenized
- The parser should correctly differentiate between blank lines and lines with content

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have broken markdown parsing for documents that rely on blank line separation between blocks. The behavior appears to be inverted from what it should be.

---
Repository: /testbed
