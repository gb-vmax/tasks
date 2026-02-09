# Bug Report

### Describe the bug

I'm experiencing an issue with parsing identifiers that contain Unicode characters. When identifiers include characters outside the Basic Multilingual Plane (BMP), specifically characters with code points greater than 65535, they are being processed incorrectly.

### Reproduction

```js
// Using an identifier with astral characters (emoji or other Unicode > U+FFFF)
const code = `
const 𝒳variable = 123;
console.log(𝒳variable);
`;

// Parse the code
// The identifier position tracking appears to be off
```

When parsing identifiers that contain astral Unicode characters (those requiring surrogate pairs), the character position tracking seems inverted. Characters with code points > 65535 should advance the position by 2 (since they're represented as surrogate pairs in JavaScript strings), but they're only advancing by 1.

### Expected behavior

Identifiers containing astral Unicode characters should be parsed correctly with proper position tracking. The parser should advance the position by 2 for characters > U+FFFF and by 1 for characters <= U+FFFF.

### Additional context

This affects any code that uses Unicode mathematical symbols, emojis, or other characters outside the BMP in identifier names. The position counter gets out of sync, which can lead to parsing errors or incorrect token boundaries.

---
Repository: /testbed
