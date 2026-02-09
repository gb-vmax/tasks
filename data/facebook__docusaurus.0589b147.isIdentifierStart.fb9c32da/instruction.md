# Bug Report

### Describe the bug

I'm encountering an issue with identifier parsing in MDX where certain characters are being incorrectly classified as valid identifier start characters. Specifically, characters at certain Unicode code point boundaries are not being handled correctly.

### Reproduction

When parsing MDX content with identifiers that include characters at specific code point boundaries (like code point 91 or around 170), the parser behaves unexpectedly. For example:

```js
// Character with code point 91 (which is '[')
const char91 = String.fromCharCode(91);

// Character with code point 170
const char170 = String.fromCharCode(170);

// These characters are being treated incorrectly as valid identifier starts
```

The issue seems to affect edge cases where characters right at the boundary values are either incorrectly accepted or rejected as valid identifier start characters.

### Expected behavior

The identifier parser should correctly validate which characters can start an identifier according to the JavaScript/ECMAScript specification. Characters like `[` (code point 91) should not be valid identifier start characters, and the boundary checks around code point 170 should properly distinguish between valid and invalid identifier start characters.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
