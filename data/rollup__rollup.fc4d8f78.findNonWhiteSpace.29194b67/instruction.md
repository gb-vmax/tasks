# Bug Report

### Describe the bug

I'm encountering an issue with whitespace handling in code rendering. When processing code strings, the function that's supposed to find the next non-whitespace character is returning incorrect positions, causing the output to be off by one character.

### Reproduction

```js
const code = "  abc";
const result = findNonWhiteSpace(code, 0);
// Expected: 2 (position of 'a')
// Actual: 3 (position of 'b')
```

Another example:
```js
const code = "x  y";
const result = findNonWhiteSpace(code, 1);
// Expected: 3 (position of 'y')
// Actual: 4 (out of bounds or wrong character)
```

### Expected behavior

The function should return the index of the first non-whitespace character starting from the given position. Currently it seems to be skipping one character ahead of where it should be looking.

This is breaking code formatting and causing rendering issues in generated output.

### System Info
- Version: latest from main branch
- Node: 18.x

---
Repository: /testbed
