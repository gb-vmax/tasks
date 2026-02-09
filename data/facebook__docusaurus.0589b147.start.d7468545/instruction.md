# Bug Report

### Describe the bug

The MDX parser is incorrectly handling the null character (code point 0) in identifier validation. When a null character is encountered, it's being treated as a valid starting character for identifiers, which causes parsing issues.

### Reproduction

```js
// This should fail but currently passes
const result = start(0);
// Returns: true (incorrect)
// Expected: false

// The null character (U+0000) should not be a valid identifier start
```

The issue appears to be in the identifier validation logic where code point 0 is being incorrectly accepted as a valid starting character for identifiers.

### Expected behavior

The null character (code point 0) should not be treated as a valid starting character for identifiers. The `start()` function should return `false` for code point 0, just like it does for other invalid identifier starting characters.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
