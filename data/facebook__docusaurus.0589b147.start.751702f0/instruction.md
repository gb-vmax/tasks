# Bug Report

### Describe the bug

I'm encountering an issue with markdown image syntax parsing where the token structure for image labels appears to be incorrect. When parsing markdown images like `![alt text](url)`, the token tree structure seems malformed.

### Reproduction

```js
// Parse a simple markdown image
const markdown = '![test image](example.png)'
const ast = parse(markdown)

// Inspecting the AST shows incorrect token nesting
// The labelImage and labelImageMarker tokens are in the wrong order
```

### Expected behavior

The token structure should properly nest `labelImage` as the parent token with `labelImageMarker` as a child token. Currently, the markers are being opened and closed in an unexpected order, which breaks the expected AST structure.

This affects any markdown processing that relies on the correct token hierarchy for images.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
