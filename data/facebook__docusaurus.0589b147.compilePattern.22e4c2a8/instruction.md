# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where special characters are being escaped incorrectly. It seems like the regex pattern compilation is treating regular characters as if they need escaping, while special regex characters are not being escaped properly.

### Reproduction

```js
// When parsing markdown with special characters
const markdown = `Some text with a period. And a dash-here.`;

// The output has unexpected escaping behavior
// Regular characters get escaped when they shouldn't
// Special regex characters don't get escaped when they should
```

### Expected behavior

The parser should:
- Escape special regex characters like `|`, `\`, `{`, `}`, `(`, `)`, `[`, `]`, `^`, `$`, `+`, `*`, `?`, `.`, `-`
- NOT escape regular alphanumeric characters
- Properly capture groups when a `before` pattern is specified

### System Info
- remark version: 15.0.1
- Node version: Latest

This appears to be a regression in the pattern compilation logic. The escaping logic seems inverted from what it should be.

---
Repository: /testbed
