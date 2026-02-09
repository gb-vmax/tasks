# Bug Report

### Describe the bug

I'm encountering an issue with character code validation in the markdown parser. When processing certain unicode characters, the parser seems to be failing to properly validate character codes, which is causing unexpected behavior when parsing markdown content.

### Reproduction

```js
// This appears to fail when processing certain character codes
const markdown = `
Some text with special characters
`;

// The parser seems to have issues with character code validation
// specifically around boundary conditions for valid character codes
```

When I try to parse markdown with certain unicode or special characters, the validation logic doesn't work as expected. It seems like the character code checking is broken - valid characters are being rejected or the validation is not handling edge cases properly.

### Expected behavior

The markdown parser should correctly validate character codes and process all valid unicode characters without issues. Character codes should be properly checked against the regex patterns.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
