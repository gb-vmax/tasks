# Bug Report

### Describe the bug

I'm experiencing an issue with whitespace handling in markdown parsing. It appears that spaces and line endings are not being recognized correctly, which is causing parsing failures for directives that should work with proper spacing.

### Reproduction

When trying to parse markdown with directives that contain spaces, the parser fails to recognize valid whitespace characters. For example:

```js
const markdown = `
::directive with spaces
content here
::
`;

// Parser fails to handle the spaces correctly
parse(markdown);
```

The same issue occurs with various whitespace scenarios:
- Regular spaces (code 32)
- Virtual spaces (code -1)
- Line feed characters (code -2)

### Expected behavior

The parser should correctly identify and handle whitespace characters including:
- Space character (ASCII 32)
- Virtual space markers (code -1)
- Line feed markers (code -2)

These should all be treated as valid markdown space characters for proper directive parsing.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This seems to have broken after a recent update. The whitespace detection logic appears to be inverted or incorrect.

---
Repository: /testbed
