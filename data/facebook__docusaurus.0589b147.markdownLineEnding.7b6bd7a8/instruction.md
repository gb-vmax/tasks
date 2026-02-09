# Bug Report

### Describe the bug
I'm encountering an issue with markdown parsing where line endings are not being detected correctly. It seems like the parser is failing to recognize certain valid line ending characters, which causes markdown content to render incorrectly or not parse at all.

### Reproduction
```js
// Parse markdown with various line endings
const markdown = `
First line
Second line

Third line after blank
`;

// The parser fails to properly detect line endings
// Resulting in incorrect parsing behavior
```

When I try to parse markdown content that contains line breaks, the output doesn't match what I expect. Lines that should be separated are being treated as continuous text, or the parser is throwing errors on valid markdown.

### Expected behavior
The parser should correctly identify all valid markdown line ending characters and handle them appropriately. Line breaks should be recognized and the content should parse correctly regardless of the line ending format used.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This seems to have started recently and is affecting markdown parsing across different files. Any help would be appreciated!

---
Repository: /testbed
