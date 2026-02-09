# Bug Report

### Describe the bug

I'm experiencing an issue with identifier continuation character validation in MDX. When using certain Unicode code points in identifiers, the validation logic appears to be failing or producing incorrect results.

### Reproduction

```js
// Example with a valid identifier continuation character
const codePoint = 0x200C; // Zero-width non-joiner
const result = cont(codePoint);

// Expected: true (this is a valid continuation character)
// Actual: behavior is inconsistent or throws an error
```

The issue seems to occur when the code is passed as a numeric code point value rather than being converted properly to a character for regex testing.

### Expected behavior

The `cont()` function should correctly validate whether a given code point represents a valid identifier continuation character according to the JavaScript/JSX specification. Valid continuation characters should return `true`, invalid ones should return `false`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
