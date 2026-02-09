# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where token positions are being calculated incorrectly. This seems to be affecting the parser's ability to correctly identify token boundaries, which leads to unexpected behavior when processing MDX content.

### Reproduction

When parsing MDX content with certain token sequences, the parser appears to be off by one character in its position tracking. This manifests as incorrect syntax highlighting, error messages pointing to wrong locations, or in some cases, parse failures.

Example:
```js
// Parse MDX content with inline expressions
const content = `
Some text {variable} more text
`;

// The parser reports incorrect position for the closing brace
// Expected position: 20
// Actual position: 21
```

### Expected behavior

Token positions should accurately reflect the actual character positions in the source text. Error messages and syntax highlighting should point to the correct locations in the MDX document.

### Additional context

This appears to have started recently and affects various MDX constructs including JSX expressions, component usage, and inline code blocks. The off-by-one error in position tracking cascades through the parsing process.

---
Repository: /testbed
