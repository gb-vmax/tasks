# Bug Report

### Describe the bug

I'm experiencing an issue with directive attribute parsing where the attributes marker is not being properly closed before entering the next state. This causes the token structure to be malformed when parsing directives with attributes.

### Reproduction

```js
// Parse a directive with attributes
const result = parse(':directive[text]{#id}')

// The attributesMarkerType token is never properly closed
// This results in incorrect token nesting
```

When parsing directives that include attributes (like `{#id}` or `{.class}`), the token structure becomes corrupted because the `attributesMarkerType` is entered but never exited before moving to the `between` state.

### Expected behavior

The `attributesMarkerType` token should be properly opened and closed before transitioning to the next parsing state. The token tree should have correct nesting with all entered tokens being properly exited.

### System Info
- remark-directive version: 3.0.0
- Parser: micromark-based

---
Repository: /testbed
