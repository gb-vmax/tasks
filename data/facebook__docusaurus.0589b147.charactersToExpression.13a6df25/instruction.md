# Bug Report

### Describe the bug

I'm experiencing an issue with character escaping in HTML entities. It seems like certain characters in a subset are not being properly converted to their regex-escaped equivalents, causing the generated regular expression to behave incorrectly.

### Reproduction

```js
const subset = ['<', '>', '&', '"', "'"];
const regex = charactersToExpression(subset);

// The regex doesn't match the first character in the subset
const testString = '<div>test</div>';
const matches = testString.match(regex);

// Expected: matches should include '<' and '>'
// Actual: first character is skipped/not matched correctly
```

When processing a subset of characters that need to be escaped for regex, the first element appears to be skipped or incorrectly handled. This causes the resulting regular expression to miss matches for the first character in the provided subset.

### Expected behavior

All characters in the subset should be properly escaped and included in the generated regular expression pattern. The regex should match all characters provided in the input subset, including the first one.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
