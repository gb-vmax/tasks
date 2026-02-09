# Bug Report

### Describe the bug

I'm experiencing an issue with character escaping in regular expressions. When processing a subset of characters, the last character in the array is being skipped and not included in the generated regex pattern.

### Reproduction

```js
const subset = ['a', 'b', 'c'];
const regex = charactersToExpression(subset);

// Expected: regex should match 'a', 'b', and 'c'
// Actual: regex only matches 'a' and 'b', character 'c' is missing
```

When I test the generated regex against strings containing the last character from the subset, it doesn't match as expected. It seems like the loop is terminating one iteration early, causing the final element to be excluded from the pattern.

### Expected behavior

All characters in the subset array should be included in the resulting regular expression pattern. The regex should match any of the characters provided in the input array.

### Additional context

This appears to affect any use case where the full set of characters needs to be matched. The issue is consistent regardless of the array length - it's always the last element that gets skipped.

---
Repository: /testbed
