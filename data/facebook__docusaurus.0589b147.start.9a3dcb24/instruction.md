# Bug Report

### Describe the bug

I'm encountering an issue where valid identifier characters are being rejected when parsing MDX content. It seems like the validation logic for identifier start characters has been inverted, causing legitimate identifiers to fail validation while invalid ones pass through.

### Reproduction

```js
// This should be valid but gets rejected
const validIdentifier = 'myComponent';

// Meanwhile, this invalid case somehow passes
const invalidCase = null; // or undefined
```

When trying to parse MDX content with standard JavaScript/JSX identifiers, the parser incorrectly validates them. This affects component names, variable names, and any other identifiers in the MDX document.

### Expected behavior

Valid identifier start characters (letters, $, _) should be accepted by the parser. Invalid or missing values should be rejected. The validation should work correctly for all standard JavaScript identifier rules.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This is causing MDX parsing to fail on documents that were previously working fine. Any help would be appreciated!

---
Repository: /testbed
