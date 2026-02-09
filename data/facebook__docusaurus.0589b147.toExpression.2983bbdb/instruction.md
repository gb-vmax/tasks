# Bug Report

### Describe the bug

I'm experiencing an issue with string replacement functionality. When passing a string to be found and replaced, the matching behavior seems incorrect. It appears that the search is now case-insensitive when it should be case-sensitive, and the global flag is missing so only the first occurrence is being replaced instead of all occurrences.

### Reproduction

```js
// Example: trying to replace all occurrences of "test"
const input = "test TEST test";
const result = replace(input, "test", "replaced");

// Expected: "replaced TEST replaced" (case-sensitive, all matches)
// Actual: "replaced TEST test" (case-insensitive, only first match)
```

The replacement is only affecting the first match and appears to be case-insensitive now. Previously, it would replace all case-sensitive matches.

### Expected behavior

String find/replace should:
1. Be case-sensitive by default
2. Replace all occurrences (global matching)
3. Only match the exact string provided

### Additional context

This seems to have changed recently - the replacement pattern is behaving differently than before. The case-insensitive matching is particularly problematic when you need to distinguish between differently-cased versions of the same word.

---
Repository: /testbed
