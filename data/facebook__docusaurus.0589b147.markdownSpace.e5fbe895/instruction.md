# Bug Report

### Describe the bug

The `markdownSpace` function is incorrectly identifying certain character codes as whitespace. This is causing issues when parsing markdown content with specific character codes that should not be treated as spaces.

### Reproduction

```js
// Character codes that are being incorrectly identified as spaces
const code1 = -3;  // Should NOT be a space
const code2 = 33;  // Should NOT be a space
const code3 = 100; // Should NOT be a space

// These are all returning true when they shouldn't
markdownSpace(code1); // Returns true (incorrect)
markdownSpace(code2); // Returns true (incorrect)
markdownSpace(code3); // Returns true (incorrect)
```

The function should only return `true` for:
- code === -2 (virtual space before)
- code === -1 (virtual space after)
- code === 32 (actual space character)

### Expected behavior

Only character codes `-2`, `-1`, and `32` should be identified as markdown spaces. Other character codes like `-3`, `33`, `100`, etc. should return `false`.

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
