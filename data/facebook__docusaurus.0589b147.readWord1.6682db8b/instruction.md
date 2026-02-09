# Bug Report

### Describe the bug

I'm encountering an issue with parsing JavaScript identifiers that contain certain Unicode characters. When using identifiers with characters in the Basic Multilingual Plane (BMP, code points U+0000 to U+FFFF), the parser seems to be incorrectly advancing the position counter, causing it to skip characters or misread the identifier.

### Reproduction

```js
// Example with a simple ASCII identifier
const myVariable = 123;

// This works fine, but when using certain Unicode characters:
const café = 456;  // Characters in BMP range
const test123 = 789;

// The parser appears to be advancing too many positions
// causing incorrect parsing behavior
```

When parsing JavaScript code with regular ASCII identifiers or identifiers containing Unicode characters in the lower range (U+0000 to U+FFFF), the parser position counter advances incorrectly, leading to parsing errors or skipped characters.

### Expected behavior

The parser should correctly handle identifiers with Unicode characters by advancing the position counter by 1 for characters in the BMP (≤ U+FFFF) and by 2 for characters outside the BMP (astral characters, > U+FFFF). Currently, it seems to always advance by 2 positions regardless of the character range.

### Additional context

This appears to affect the `readWord1` function in the JavaScript parser. The issue manifests when reading identifier names that contain regular ASCII or BMP Unicode characters, where the position should only increment by 1, not 2.

---
Repository: /testbed
