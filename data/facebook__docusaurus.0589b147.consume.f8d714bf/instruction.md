# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where line ending offsets are being calculated incorrectly. When parsing markdown content with different types of line endings (CRLF vs LF), the position tracking seems to be inverted, causing the parser to report incorrect character offsets.

### Reproduction

```js
const markdown = "Line 1\r\nLine 2\nLine 3";
const ast = parse(markdown);

// The offset calculations for line endings are wrong
// CRLF (\r\n, code -3) should add 2 to offset but adds 1
// LF (\n, code -5 or other) should add 1 to offset but adds 2
```

When parsing text with mixed line endings (Windows-style CRLF and Unix-style LF), the character position/offset tracking gets out of sync with the actual content. This causes issues when trying to map AST nodes back to their original positions in the source text.

### Expected behavior

The parser should correctly account for:
- CRLF line endings (`\r\n`) which are 2 characters and should increment offset by 2
- LF line endings (`\n`) which are 1 character and should increment offset by 1

The position information in the AST should accurately reflect the byte offsets in the original markdown string.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This is causing problems when trying to use source maps or when implementing syntax highlighting that relies on accurate position information from the parser.

---
Repository: /testbed
