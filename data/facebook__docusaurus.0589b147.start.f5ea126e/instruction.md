# Bug Report

### Describe the bug

I'm encountering an issue with directive attribute parsing where the attributes marker type doesn't seem to be properly closed. The parser appears to be skipping the exit call for the attributes marker, which is causing issues with the AST structure.

### Reproduction

```js
// When parsing a directive with attributes like:
::directive[text]{#id .class}

// The attributesMarkerType node is entered but never properly exited
// This causes the AST to have an incomplete/malformed structure
```

### Expected behavior

The attributes marker should be properly entered and exited in the token stream, maintaining the correct AST structure. The `effects.exit(attributesMarkerType)` should be called after consuming the opening bracket character.

### System Info
- remark-directive version: 3.0.0
- Parser: micromark-based

---
Repository: /testbed
