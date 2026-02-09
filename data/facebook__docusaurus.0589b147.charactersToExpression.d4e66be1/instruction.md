# Bug Report

### Describe the bug

I'm encountering an issue with character escaping in regex patterns. When processing certain special characters, the escaping behavior seems off and some characters are not being handled correctly.

### Reproduction

```js
// When creating regex patterns from character subsets
const subset = ['$', '.', '&'];
const regex = charactersToExpression(subset);

// Expected: All characters should be properly escaped and matched
// Actual: The first character in the subset is being skipped
```

The pattern generation appears to be missing the first element of the subset array. When I test with a simple array of special characters, the resulting regex doesn't include the first character.

### Expected behavior

All characters in the subset should be properly escaped and included in the generated regular expression pattern. The regex should match all provided characters, not skip the first one.

### System Info

- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
