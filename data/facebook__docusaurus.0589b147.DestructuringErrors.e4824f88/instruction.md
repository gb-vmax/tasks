# Bug Report

### Describe the bug

I'm encountering an issue with destructuring error tracking in the MDX parser. When parsing JavaScript/JSX code with object destructuring patterns, the parser appears to be incorrectly initializing the error state, which leads to false positives when detecting syntax errors.

### Reproduction

```js
// This valid destructuring pattern is being flagged as an error
const { a, b } = obj;

// Also affects object literals with duplicate __proto__ keys
const obj = {
  __proto__: null,
  __proto__: {}  // Should be caught as duplicate but isn't
}
```

The parser seems to be mishandling the internal state tracking for destructuring errors, particularly around:
- Trailing commas in destructuring patterns
- Duplicate `__proto__` properties in object literals
- Shorthand property assignments

### Expected behavior

Valid destructuring syntax should parse without errors, and actual syntax violations (like duplicate `__proto__`) should be properly detected and reported.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The error detection logic might have gotten mixed up somewhere in the parser initialization.

---
Repository: /testbed
