# Bug Report

### Describe the bug

After a recent update, I'm seeing unexpected behavior with markdown parsing where certain control characters and special codes are being treated as whitespace when they shouldn't be. This is causing issues with content that contains specific character codes in the range between -2 and 32.

### Reproduction

When parsing markdown content that includes character codes in the numeric range, the parser now incorrectly identifies characters as spaces. For example:

```js
// Character codes like 0, 1, 2, etc. up to 31 are now treated as spaces
// but they should not be (only -2, -1, and 32 should be considered spaces)

// This affects parsing of content with control characters
const content = "text\x00more text"; // \x00 is character code 0
// The parser now treats this as whitespace when it shouldn't
```

### Expected behavior

Only character codes -2, -1, and 32 should be treated as markdown spaces. Other character codes in between (like 0-31) should not be considered whitespace by the markdown space check function.

### System Info
- remark-mdx version: 3.0.0
- This started happening after the latest update

---
Repository: /testbed
