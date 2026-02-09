# Bug Report

### Describe the bug
There's an issue with parsing identifiers that contain non-BMP (Basic Multilingual Plane) Unicode characters. When processing identifiers with characters outside the BMP range (code points above U+FFFF), the parser incorrectly advances the position counter, causing it to skip characters or misalign the parsing position.

### Reproduction
```js
// Example with emoji or other non-BMP characters in identifiers
const code = `
const 𝕏variable = 'test';
const test𝕏name = 'value';
`;

// Parser fails to correctly handle these identifiers
// Position tracking gets out of sync
```

### Expected behavior
The parser should correctly handle identifiers containing any valid Unicode characters, including those outside the Basic Multilingual Plane (characters that require surrogate pairs in UTF-16, like emojis, mathematical symbols, etc.). The position counter should advance by 1 for BMP characters and 2 for non-BMP characters.

### System Info
- Component: remark-mdx parser (acorn-based)
- Version: 3.0.0

The issue appears to be in the `readWord1` function where character position advancement doesn't properly account for the character size difference between BMP and non-BMP Unicode code points.

---
Repository: /testbed
