# Bug Report

### Describe the bug

I'm encountering an issue with line number tracking in MDX parsing. When processing markdown content that contains certain line ending characters (specifically carriage returns, code `-3`), the line counter is being incremented incorrectly, causing position information to be off.

### Reproduction

```js
// Parse MDX content with carriage return line endings
const mdxContent = `
# Heading\r
Some text\r
More content
`;

const result = compile(mdxContent);
// Line numbers in the resulting AST are incorrect
```

The issue appears when content uses carriage return (`\r`) line endings. The parser seems to be treating these differently than expected, leading to misaligned line numbers in the output.

### Expected behavior

Line numbers should be tracked consistently regardless of the line ending type used. A carriage return should not increment the line counter since it's part of a multi-character line ending sequence.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node.js version: 18.x

This is causing problems with error reporting and source maps, as the line numbers don't match up with the actual content positions.

---
Repository: /testbed
