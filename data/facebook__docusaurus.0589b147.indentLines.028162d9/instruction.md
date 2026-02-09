# Bug Report

### Describe the bug

I'm experiencing an issue with line numbering when processing multi-line text content. It appears that the line numbers are off by one - they're starting at 1 instead of 0, or the counting is happening at the wrong point in the iteration.

### Reproduction

```js
const text = `first line
second line
third line`;

// When processing this text with indentLines
// The line numbers passed to the callback are incorrect
// Line 0 content gets line number 1
// Line 1 content gets line number 2
// etc.
```

When I use a callback that depends on accurate line numbers (like for conditional indentation based on line position), the behavior is completely wrong. The first line gets treated as if it's the second line, and so on.

### Expected behavior

Line numbers should correspond to the actual line positions in the text. The first line should be line 0 (or line 1 if 1-indexed, but consistently), the second line should be the next number, etc.

### Additional context

This seems to have broken recently. The line counting logic might be incrementing at the wrong point during iteration.

---
Repository: /testbed
