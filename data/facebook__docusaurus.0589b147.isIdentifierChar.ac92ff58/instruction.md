# Bug Report

### Describe the bug

I'm experiencing an issue with identifier parsing in MDX. It appears that certain characters that should not be valid in JavaScript identifiers are being incorrectly accepted as valid identifier characters.

Specifically, the colon character `:` (character code 58) and the opening square bracket `[` (character code 91) are being treated as valid identifier characters when they shouldn't be according to JavaScript identifier naming rules.

### Reproduction

```js
// These should not be valid identifiers but are being accepted:
const test:name = "value";  // colon should not be allowed
const test[name = "value";  // opening bracket should not be allowed
```

When parsing MDX content that includes these edge case characters, the parser doesn't properly reject them as invalid identifier characters.

### Expected behavior

The identifier character validation should correctly reject:
- Character code 58 (`:` colon)
- Character code 91 (`[` opening square bracket)

These characters fall just outside the valid ASCII ranges for identifier characters:
- Digits: 48-57 (0-9)
- Uppercase letters: 65-90 (A-Z)

The parser should only accept characters within these ranges (plus `$` at code 36), not the boundary characters themselves.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
