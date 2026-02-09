# Bug Report

### Describe the bug

I'm encountering an issue with whitespace handling in code rendering. When trying to find the last whitespace character in reverse, the function seems to be returning incorrect positions, causing text to be truncated or split at the wrong locations.

### Reproduction

```js
const code = "function test() { return true; }";
const start = 0;
const end = 20;

// Expected to find whitespace position correctly
const result = findLastWhiteSpaceReverse(code, start, end);

// Result is off by one position
console.log(result); // Returns unexpected position
```

The issue appears when the function searches backwards for whitespace characters. It's not correctly identifying the boundary position, which leads to incorrect string splitting behavior.

### Expected behavior

The function should accurately locate the last whitespace character when searching in reverse from a given end position. The returned index should point to the correct character position for proper text wrapping or code formatting.

### Additional context

This is affecting code formatting features where lines need to be broken at appropriate whitespace boundaries. The current behavior sometimes includes or excludes characters that shouldn't be part of the split.

---
Repository: /testbed
