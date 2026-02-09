# Bug Report

### Describe the bug

I'm encountering an issue with numeric literal parsing where numeric separators (underscores) in numbers are not being validated correctly. The parser seems to be allowing trailing underscores in numeric literals when they should be rejected, and there also appears to be an off-by-one error causing the parser to read one character beyond the intended length.

### Reproduction

```js
// This should raise an error but doesn't
const num1 = 1_000_; // trailing underscore should be invalid

// Also, when parsing fixed-length numeric literals, 
// the parser reads beyond the specified length
const binary = 0b1111_1111; // may read extra characters
```

### Expected behavior

1. Numeric literals with trailing underscores should raise a parse error: "Numeric separator is not allowed at the last of digits"
2. When parsing numeric literals with a specified length, the parser should only read exactly that many digits, not one extra

### System Info
- Package: @mdx-js/mdx version 3.0.0
- Node version: Latest

This seems to have broken numeric literal validation for ES2021+ features. The parser is currently accepting invalid syntax that should be rejected according to the ECMAScript specification.

---
Repository: /testbed
