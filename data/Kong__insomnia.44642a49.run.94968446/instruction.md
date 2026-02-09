# Bug Report

### Describe the bug

I'm encountering an issue with base64 encoding where non-ASCII characters (like Chinese, Japanese, or characters with accents) are not being encoded correctly. The encoded output appears corrupted and when decoded back, the original text is lost or garbled.

### Reproduction

```js
// Example with Chinese characters
const text = "你好世界";
const encoded = base64Encode(text, 'normal');
const decoded = base64Decode(encoded);
// Expected: "你好世界"
// Actual: garbled or incorrect output

// Example with accented characters
const text2 = "café résumé";
const encoded2 = base64Encode(text2, 'normal');
const decoded2 = base64Decode(encoded2);
// Expected: "café résumé"
// Actual: incorrect characters
```

Steps to reproduce:
1. Use the base64 template tag with text containing non-ASCII characters
2. Encode the text using 'normal' mode
3. Try to decode it back
4. The result doesn't match the original input

This seems to affect various character sets including:
- Chinese/Japanese characters
- Accented Latin characters (é, ñ, ü, etc.)
- Emoji and other Unicode characters

The issue appears to be related to character encoding detection or handling during the encoding process. ASCII-only text works fine, but anything outside the ASCII range gets corrupted.

### Expected behavior

Base64 encoding should handle all Unicode characters correctly and preserve them when encoding/decoding, regardless of the character set used.

---
Repository: /testbed
