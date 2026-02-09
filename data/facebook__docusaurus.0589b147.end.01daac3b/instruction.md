# Bug Report

### Describe the bug

I'm experiencing an issue with HTML text parsing where malformed HTML tags (specifically those missing a closing `>`) are being accepted instead of being rejected. This appears to be a regression in the HTML tokenization logic.

### Reproduction

```js
// This should fail but doesn't
const input = '<span class="test"'  // Missing closing >

// Parser accepts this malformed HTML instead of rejecting it
```

When processing HTML text that's missing the closing angle bracket, the parser should reject it but instead it's being accepted as valid. This can lead to incorrect parsing of markdown documents containing malformed HTML.

### Expected behavior

The parser should reject HTML tags that don't have a proper closing `>` character. Malformed HTML should not be silently accepted.

### Additional context

This seems to affect the HTML text tokenization specifically. The issue appears to be in how the end of HTML tags is validated - it's not properly checking for the closing bracket before accepting the token.

---
Repository: /testbed
