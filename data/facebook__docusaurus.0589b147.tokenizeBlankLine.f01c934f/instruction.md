# Bug Report

### Describe the bug

I'm experiencing an issue with blank line parsing in markdown. The parser seems to be getting stuck in an infinite loop or incorrectly handling certain blank line scenarios. When processing markdown content with specific whitespace patterns, the parser either hangs or produces unexpected results.

### Reproduction

```js
// Example markdown content that triggers the issue
const markdown = `
Some text

    
More text
`;

// Parser gets stuck or produces incorrect output
const result = parse(markdown);
```

### Expected behavior

The parser should correctly identify and process blank lines, distinguishing between:
1. Lines with only whitespace characters
2. Completely empty lines
3. Lines that are part of code blocks or other structures

The parser should handle these cases without hanging and produce the expected AST structure.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
