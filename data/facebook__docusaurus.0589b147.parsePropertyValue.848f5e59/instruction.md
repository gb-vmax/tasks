# Bug Report

### Describe the bug

I'm experiencing issues with object destructuring patterns when they include default values. The parser seems to be incorrectly handling the assignment of values in destructuring patterns versus regular object literals.

### Reproduction

```js
// This destructuring pattern with defaults is not being parsed correctly
const { a: b = 5 } = obj;

// Also seeing issues with shorthand property assignments in destructuring
const { x = 10 } = data;
```

When using destructuring patterns with colons (renaming) and default values, the parser appears to swap the logic for when to apply default value parsing versus regular assignment parsing.

### Expected behavior

The parser should correctly distinguish between:
1. Destructuring patterns (which can have default values)
2. Regular object property assignments

Destructuring patterns like `{ a: b = 5 }` should properly parse the default value on the right side of the colon.

### Additional context

This appears to affect the parsing logic for object properties, specifically around how the parser determines whether to use `parseMaybeDefault` or `parseMaybeAssign` based on whether we're in a pattern context.

---
Repository: /testbed
