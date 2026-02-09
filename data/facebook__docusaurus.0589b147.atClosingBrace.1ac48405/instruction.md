# Bug Report

### Describe the bug

I'm encountering an issue with directive label parsing where the closing brace marker isn't being properly entered before consumption. This causes the token stream to be malformed when parsing directives with labels.

### Reproduction

```js
// Parse a directive with a label
const directive = ':directive[label text]{}'

// The closing brace marker token is consumed without being entered first
// This breaks the token tree structure
```

When processing directives that contain labels (text within square brackets), the closing brace `]` is consumed but the marker token isn't properly entered into the effects stream before consumption. This results in an unbalanced token tree.

### Expected behavior

The closing brace marker should be entered via `effects.enter(markerType)` before being consumed with `effects.consume(code)`, similar to how other markers are handled throughout the parser. The token stream should maintain proper enter/exit pairs for all tokens.

### System Info
- remark-directive version: 3.0.0
- Parser: micromark-extension-directive

---
Repository: /testbed
