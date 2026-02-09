# Bug Report

### Describe the bug

I'm encountering an issue with the MDX parser where position tracking seems to be broken. When parsing MDX content, the parser is no longer able to determine the current position in the source code, which is causing problems with error reporting and source maps.

### Reproduction

```js
const mdx = `
# Hello World

Some content here
`;

const result = parseMDX(mdx);
// Parser fails to track positions correctly
// Error messages don't show line/column information
```

### Expected behavior

The parser should correctly track the current position (line and column) in the source file during parsing. This is essential for:
- Accurate error messages with line/column numbers
- Source map generation
- Debugging MDX syntax issues

### Additional context

This appears to affect the `curPosition` functionality in the acorn parser integration. The position tracking was working in previous versions but seems to have regressed recently.

---
Repository: /testbed
