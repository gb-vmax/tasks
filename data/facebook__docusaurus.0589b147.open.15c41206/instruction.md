# Bug Report

### Describe the bug
Image syntax in markdown is not being parsed correctly. When trying to use the standard markdown image syntax `![alt text](url)`, the parser fails to recognize it properly.

### Reproduction
```js
const markdown = '![test image](https://example.com/image.png)'

// Parser doesn't recognize this as an image
// Expected: Image node in AST
// Actual: Invalid/malformed parse result
```

### Expected behavior
The markdown parser should correctly parse image syntax that starts with `![` and treat it as an image node. The opening bracket `[` after the exclamation mark should be recognized as the start of the alt text.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have broken recently - standard markdown image syntax is no longer working as expected.

---
Repository: /testbed
