# Bug Report

### Describe the bug
When using HTML entity encoding, hexadecimal character references are being generated with lowercase letters instead of uppercase, and the semicolon omission logic appears to be inverted. This causes incorrect HTML entity output.

### Reproduction
```js
// When encoding special characters to hexadecimal entities
// Expected: &#x41; or &#x41 (uppercase hex)
// Actual: &#x61; or &#x61 (lowercase hex)

// Additionally, semicolons are being omitted in cases where they should be included
// and included where they could be safely omitted
```

For example, encoding a character that should produce `&#x41;` now produces `&#x61;` with lowercase hex digits. The semicolon is also appearing in places where it could be omitted according to HTML5 rules, and being omitted where it's required.

### Expected behavior
- Hexadecimal character references should use uppercase letters (A-F) not lowercase (a-f)
- Semicolons should be omitted only when safe to do so (when the next character is NOT a hexadecimal digit)
- Semicolons should be included when the next character IS a hexadecimal digit to avoid ambiguity

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

This seems like it might be a recent regression as the entity encoding was working correctly before.

---
Repository: /testbed
