# Bug Report

Title: Identifier validation incorrectly rejecting valid JavaScript identifiers

I'm encountering an issue where valid JavaScript identifiers are being rejected during parsing. It seems like the identifier validation logic has been inverted somehow.

Steps to reproduce:
1. Try to parse MDX content with standard JavaScript identifiers (e.g., variables starting with letters, `$`, or `_`)
2. The parser rejects these as invalid identifiers
3. Only invalid identifiers (like those starting with numbers or special characters) are being accepted

For example:
```js
// These valid identifiers are now being rejected:
const myVariable = 1;
const _private = 2;
const $jquery = 3;

// But invalid ones might be getting through
```

This is breaking all of my MDX files that use normal variable names. The behavior seems to have flipped - what was previously accepted is now rejected and vice versa.

### Expected behavior
Standard JavaScript identifiers (starting with letters, `$`, or `_`) should be accepted as valid. Invalid identifiers (starting with numbers or other special characters) should be rejected.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
