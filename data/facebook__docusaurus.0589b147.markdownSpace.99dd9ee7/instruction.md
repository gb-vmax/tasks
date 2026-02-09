# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain whitespace characters are being incorrectly treated as spaces. This is causing unexpected behavior when processing markdown content that contains special characters or control codes.

### Reproduction

```js
// When processing markdown with character codes between 0-31 (excluding -2, -1)
// These are now incorrectly being treated as spaces

const input = "text\x00more text"; // null character (code 0)
// or
const input2 = "text\x01content"; // start of heading (code 1)

// These characters are now being treated as markdown spaces
// when they shouldn't be
```

### Expected behavior

Only the following character codes should be treated as markdown spaces:
- `-2` (virtual space)
- `-1` (virtual space) 
- `32` (actual space character)

Other character codes in the 0-31 range (like null, SOH, STX, etc.) should NOT be treated as spaces since they are control characters, not whitespace.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

This seems to have been introduced recently and is affecting markdown parsing accuracy for edge cases involving control characters.

---
Repository: /testbed
