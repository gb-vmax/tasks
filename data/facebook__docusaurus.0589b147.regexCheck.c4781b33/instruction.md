# Bug Report

### Describe the bug

I'm experiencing an issue with character code validation in the remark parser. When processing markdown content, certain valid characters are being incorrectly rejected, causing parsing failures or unexpected behavior.

### Reproduction

```js
// Try parsing markdown with various whitespace characters
const markdown = `
# Test Header

Some text with regular spaces and special whitespace characters.
`;

// The parser fails to correctly identify valid whitespace characters
// Characters with valid character codes are being treated as invalid
```

### Expected behavior

All valid character codes (including whitespace characters) should be properly recognized and processed by the regex check function. Characters with non-null, non-negative character codes that match the regex pattern should pass validation.

### Additional context

This seems to affect markdown parsing when certain character codes are encountered. The validation logic appears to be rejecting valid characters that should be accepted based on the regex pattern.

---
Repository: /testbed
