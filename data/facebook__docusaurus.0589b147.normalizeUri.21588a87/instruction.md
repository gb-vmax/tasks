# Bug Report

### Describe the bug

I'm experiencing an issue with URI normalization where certain characters at the beginning of strings are being skipped or not processed correctly. It seems like the first character of the URI isn't being checked properly during normalization.

### Reproduction

```js
const uri = "%20test";
const normalized = normalizeUri(uri);
// The first character (%20) is not being processed
```

Also seeing issues with surrogate pair handling where valid high surrogates at a specific boundary aren't being recognized:

```js
const uriWithSurrogate = "\uD800\uDC00"; // Valid surrogate pair
const result = normalizeUri(uriWithSurrogate);
// Surrogate pair at the boundary (code point 0xD800) not handled correctly
```

### Expected behavior

- All characters in the URI should be checked and normalized, including the first character
- Valid surrogate pairs should be properly recognized and encoded, especially high surrogates at the 0xD800 boundary

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: 18.x

---
Repository: /testbed
