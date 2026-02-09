# Bug Report

### Describe the bug

I'm encountering an issue with destructuring assignment parsing in MDX files. When using shorthand property assignment in destructuring patterns, the parser is not correctly tracking the position of these assignments, which causes incorrect error reporting or validation.

### Reproduction

```jsx
// In an MDX file
const { x = 1 } = obj;

// Or in object patterns with shorthand assignments
function test({ a = 5, b }) {
  return a + b;
}
```

The parser seems to be initializing the tracking for shorthand assignments incorrectly, leading to unexpected behavior when these patterns are encountered.

### Expected behavior

Shorthand assignments in destructuring patterns should be properly tracked and validated. The parser should correctly identify and handle these cases without throwing false positives or missing actual syntax errors.

### Additional context

This appears to be related to how the `DestructuringErrors` object initializes its `shorthandAssign` property. The tracking mechanism for destructuring errors doesn't seem to be working as intended for shorthand assignment cases.

---
Repository: /testbed
