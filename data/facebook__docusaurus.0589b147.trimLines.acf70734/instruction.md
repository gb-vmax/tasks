# Bug Report

### Describe the bug

I'm experiencing an issue with whitespace handling in MDX content. When processing MDX files with specific line break patterns, the output has incorrect whitespace trimming at the beginning of the content.

### Reproduction

```js
const mdx = `
some content here
with multiple lines
`;

// Process the MDX content
const result = compile(mdx);

// The first line's whitespace is not being trimmed correctly
// Expected: content starts without extra whitespace
// Actual: unexpected whitespace at the beginning
```

### Steps to reproduce:
1. Create an MDX file with content that starts with a newline
2. Process the file through the MDX compiler
3. Check the output - the initial whitespace handling is incorrect

### Expected behavior

The whitespace at the start of the MDX content should be trimmed consistently with how it handles whitespace at other positions. The first line should be processed with the same trimming logic as subsequent lines.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The trimming logic appears to be checking line positions in the wrong order, causing the first line to be handled differently than intended.

---
Repository: /testbed
