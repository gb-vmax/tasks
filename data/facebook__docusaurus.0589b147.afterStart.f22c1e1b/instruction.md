# Bug Report

### Describe the bug
When parsing directive labels with empty content (e.g., `[]`), the parser produces incorrect AST structure. The string type token is being entered but never exited when the label is empty, which breaks the token hierarchy.

### Reproduction
```js
// Parse a directive with an empty label
const input = ':directive[]'

// The resulting AST has malformed token structure
// Expected: proper nesting with markerType tokens wrapping an empty stringType
// Actual: stringType token is entered but not properly closed
```

### Expected behavior
Empty directive labels should be parsed correctly with proper token entry/exit order. The AST should maintain correct nesting even when the label content is empty.

### Additional context
This appears to affect directives that use the bracket notation for labels. When the closing bracket immediately follows the opening bracket (empty label case), the token structure becomes inconsistent.

---
Repository: /testbed
