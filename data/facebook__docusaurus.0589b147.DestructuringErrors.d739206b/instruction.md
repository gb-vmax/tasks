# Bug Report

### Describe the bug

I'm experiencing an issue with parsing destructuring assignments in MDX files. When using parenthesized assignment patterns, the parser is incorrectly flagging valid syntax as errors or not properly tracking assignment positions.

### Reproduction

```js
// This valid destructuring pattern causes issues
const obj = {};
({a: obj.a} = {a: 1});

// Or with trailing commas in destructuring
const {x, y,} = {x: 1, y: 2};
```

When these patterns are used in MDX content, the parser behaves unexpectedly and may not correctly handle the destructuring syntax.

### Expected behavior

The parser should correctly handle parenthesized assignments and trailing commas in destructuring patterns without throwing errors or misidentifying token positions.

### System Info
- MDX version: 3.0.0
- Node version: Latest

This seems related to how the `DestructuringErrors` object is initialized. The tracking of `parenthesizedAssign` might not be starting from the correct initial value.

---
Repository: /testbed
