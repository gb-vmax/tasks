# Bug Report

### Describe the bug

I'm encountering an issue with identifier parsing in MDX content. When processing certain code points, the parser seems to fail or behave unexpectedly. It looks like there's a problem with how character codes are being validated as valid identifier start characters.

### Reproduction

```js
// This causes unexpected behavior
const code = 0x1F4A9; // or other numeric code points
// Parser fails to correctly identify valid identifier start characters
```

The issue appears when numeric code values are passed to the identifier validation logic. Instead of properly checking if a code point represents a valid identifier start character, it seems to be converting the numeric value incorrectly.

### Expected behavior

The parser should correctly validate whether a given code point can start an identifier according to Unicode standards. Numeric code points should be properly converted to their string representation before regex testing.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
